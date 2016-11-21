import argparse
import py_compile
import re
import sys
import shutil
import stat
import os
import tempfile

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

PY34 = sys.version_info > (3, 3)

EXCLUDE_FROM_LIBRARY = {
    if PY34:
        'asyncio',
    '_cffi_backend',
    'aiohttp',
    'yarl',
    'pycares',
    'cchardet',
    'nacl',
    'multidict',
}


def include_in_lib(p):
    name = p.name.lower()
    if p.is_dir():
        if name in EXCLUDE_FROM_LIBRARY:
            return False
        if name.startswith('plat-'):
            return False
        if name == 'test' and p.parts[-2].lower() == 'lib':
            return False
        if name in {'test', 'tests'} and p.parts[-3].lower() == 'lib':
            return False
        return True

    suffix = p.suffix.lower()
    return suffix not in {'.pyc', '.pyo', '.exe', '.pyd', '.so'}


EMBED_LAYOUT = [
    ('dependencies.{0}.{1.name}-{2.major}{2.minor}{2.micro}.zip'.format(sys.platform, sys.implementation, sys.version_info), 'Lib', '**/*', include_in_lib),
]


def copy_to_layout(target, rel_sources):
    count = 0

    if target.suffix.lower() == '.zip':
        if target.exists():
            target.unlink()

        with ZipFile(str(target), 'w', ZIP_DEFLATED) as f:
            with tempfile.TemporaryDirectory() as tmpdir:
                for s, rel in rel_sources:
                    if rel.suffix.lower() == '.py':
                        pyc = Path(tmpdir) / rel.with_suffix('.pyc').name
                        try:
                            py_compile.compile(str(s), str(pyc), str(rel), doraise=True, optimize=2)
                        except py_compile.PyCompileError:
                            f.write(str(s), str(rel))
                        else:
                            f.write(str(pyc), str(rel.with_suffix('.pyc')))
                    else:
                        f.write(str(s), str(rel))
                    count += 1

    else:
        for s, rel in rel_sources:
            dest = target / rel
            try:
                dest.parent.mkdir(parents=True)
            except FileExistsError:
                pass
            if dest.is_file():
                dest.chmod(stat.S_IWRITE)
            shutil.copy(str(s), str(dest))
            if dest.is_file():
                dest.chmod(stat.S_IWRITE)
            count += 1

    return count


def rglob(root, pattern, condition):
    dirs = [root]
    recurse = pattern[:3] in {'**/', '**\\'}
    while dirs:
        d = dirs.pop(0)
        for f in d.glob(pattern[3:] if recurse else pattern):
            if recurse and f.is_dir() and (not condition or condition(f)):
                dirs.append(f)
            elif f.is_file() and (not condition or condition(f)):
                yield f, f.relative_to(root)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', metavar='dir', help='The directory containing the repository root', type=Path)
    parser.add_argument('-o', '--out', metavar='file', help='The name of the output archive', type=Path, default=None)
    parser.add_argument('-t', '--temp', metavar='dir', help='A directory to temporarily extract files into', type=Path, default=None)
    ns = parser.parse_args()

    source = ns.source or (Path(__file__).resolve().parent.parent.parent)
    out = ns.out
    assert isinstance(source, Path)
    assert not out or isinstance(out, Path)

    if ns.temp:
        temp = ns.temp
        delete_temp = False
    else:
        temp = Path(tempfile.mkdtemp())
        delete_temp = True

    if out:
        try:
            out.parent.mkdir(parents=True)
        except FileExistsError:
            pass
    try:
        temp.mkdir(parents=True)
    except FileExistsError:
        pass

    layout = EMBED_LAYOUT

    try:
        if out:
            total = copy_to_layout(out, rglob(temp, '**/*', None))
            print('Wrote {} files to {}'.format(total, out))
    finally:
        if delete_temp:
            try:
                shutil.rmtree(temp, True)
            except TypeError:
                pass


if __name__ == "__main__":
    sys.exit(int(main() or 0))
