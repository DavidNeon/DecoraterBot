# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2016 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
try:
    from . import api
except SystemError:
    import py2pycx.api
import sys
import getopt


def main(argv):
    """..."""
    if len(argv) < 1:
        sys.exit(2)
    try:
        options, arguments = getopt.getopt(argv, 'p:f:c:a:', ['path=', 'filename=', 'compression_level=', 'password='])
    except getopt.GetoptError:
        sys.exit(2)
    in_path = None
    filename = None
    czlevel = None
    pswd = None
    for option, argument in options:
        if option in ('p', '--path'):
            in_path = argument
        if option in ('f', '--filename'):
            filename = argument
        if option in ('c', '--compression-level'):
            czlevel = argument
        if option in ('a', '--password'):
            pswd = argument
    if pswd is not None:
        try:
            api.compress_protected_script(in_path, filename, cz_level=czlevel, password=pswd)
            print('Password Protected Script Compression Complete.')
        except api.NoPasswordSpecified as err:
            print('Error: {0}'.format(str(err)))
        except api.FileNotFound as err:
            print('Error: {0}'.format(str(err)))
        except api.FilePathNotProvided as err:
            print('Error: {0}'.format(str(err)))
        except api.FileNameNotProvided as err:
            print('Error: {0}'.format(str(err)))
    else:
        try:
            api.compress_script(in_path, filename, cz_level=czlevel)
            print('Script Compression Complete.')
        except api.FileNotFound as err:
            print('Error: {0}'.format(str(err)))
        except api.FilePathNotProvided as err:
            print('Error: {0}'.format(str(err)))
        except api.FileNameNotProvided as err:
            print('Error: {0}'.format(str(err)))

if __name__ == "__main__":
    main(sys.argv[1:])
