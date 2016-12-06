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
import base64
import io
import zlib


class BaseErrors(Exception):
    """
    Base Exceptions class.
    """
    pass


class FilePathNotProvided(BaseErrors):
    """
    Exception for When a Script File (Either Compressed or not) is not provided.
    """
    pass


class FileNameNotProvided(BaseErrors):
    """
    Exception for When a Script File is not provided is not provided.
    """
    pass


class FileNotFound(BaseErrors):
    """
    Exception for When a Script File (Either Compressed or not) is not found.
    """
    pass


class NoPasswordSpecified(BaseErrors):
    """
    Exception for When a Password is not specified for a Password Protected Script file.
    """
    pass


class InvalidPassword(BaseErrors):
    """
    Exception for when a Password is Incorrect.
    """
    pass


class PasswordProtectedError(BaseErrors):
    """
    Exception for when Trying to Decompress a Password Protected file in the Non-Password Protection
    version of the Decompressor.
    """
    pass


class NoPasswordPresent(BaseErrors):
    """
    Exception for when the Password Protected Decompress Function is Called with a PYCX file that has
    no password protection on it.
    """
    pass


class DecompressionError(BaseErrors):
    """
    Exception for when a zlib Error for depmpressing a pycx or pyccx file happens.
    """
    pass


def compress_script(filepath, filename, cz_level=None):
    """
    Compresses a Python Script.
    :param filepath: Path to the file to compress.
    :param filename: File name to compress.
    :param cz_level: Compression level (Max is 9) If None is provided then default is level 9.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if cz_level is None:
                cz_level = 9
            filedata = None
            try:
                file = io.open(filepath + filename + '.py', "rb")
                if file is not None:
                    filedata = file.read()
                    file.close()
                base64data = base64.b64encode(filedata)
                czfiledata = b'PYCX' + zlib.compress(base64data, cz_level)
                czfileobj = open(filepath + filename + '.pycx', 'wb')
                if czfileobj is not None:
                    czfileobj.write(czfiledata)
                    czfileobj.close()
            except FileNotFoundError:
                notfound = True
            if notfound:
                raise FileNotFound('{0}.py was not found.'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to compress a python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to compress a python script file.')


def compress_protected_script(filepath, filename, cz_level=None, password=None):
    """
    Same as compress_script() but is for Compressing password Protected pycx files.

    Password must be a byte string. This Function will then add the byte string in to the
    file (in a compressed form ofc).
    :param filepath: Path to the file to compress.
    :param filename: File name to compress.
    :param cz_level: Compression level (Max is 9) If None is provided then default is level 9.
    :param password: Compression Password to use to encode into the processed file.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = b'&pw=' + base64.b64encode(password)
                if cz_level is None:
                    cz_level = 9
                filedata = None
                try:
                    file = io.open(filepath + filename + '.py', "rb")
                    if file is not None:
                        filedata = file.read()
                        file.close()
                    base64data = base64.b64encode(filedata)
                    czfiledata = b'PYCX' + pswdata + zlib.compress(base64data, cz_level)
                    czfileobj = open(filepath + filename + '.pycx', 'wb')
                    if czfileobj is not None:
                        czfileobj.write(czfiledata)
                        czfileobj.close()
                except FileNotFoundError:
                    notfound = True
                if notfound:
                    raise FileNotFound('{0}.py was not found.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to compress {0}.pycx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to compress a python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to compress a python script file.')


def compress_bytecode(filepath, filename, cz_level=None):
    """
    Compresses a Python pyc file.
    :param filepath: Path to the file to compress.
    :param filename: File name to compress.
    :param cz_level: Compression level (Max is 9) If None is provided then default is level 9.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if cz_level is None:
                cz_level = 9
            filedata = None
            try:
                file = io.open(filepath + filename + '.pyc', "rb")
                if file is not None:
                    filedata = file.read()
                    file.close()
                base64data = base64.b64encode(filedata)
                czfiledata = b'PYCCX' + zlib.compress(base64data, cz_level)
                czfileobj = open(filepath + filename + '.pyccx', 'wb')
                if czfileobj is not None:
                    czfileobj.write(czfiledata)
                    czfileobj.close()
            except FileNotFoundError:
                notfound = True
            if notfound:
                raise FileNotFound('{0}.pyc was not found.'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to compress a python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to compress a python Bytecode file.')


def compress_protected_bytecode(filepath, filename, cz_level=None, password=None):
    """
    Same as compress_bytecode() but is for Compressing password Protected pyccx files.

    Password must be a byte string. This Function will then add the byte string in to the
    file (in a compressed form ofc).
    :param filepath: Path to the file to compress.
    :param filename: File name to compress.
    :param cz_level: Compression level (Max is 9) If None is provided then default is level 9.
    :param password: Compression Password to use to encode into the processed file.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = b'&pw=' + base64.b64encode(password)
                if cz_level is None:
                    cz_level = 9
                filedata = None
                try:
                    file = io.open(filepath + filename + '.pyc', "rb")
                    if file is not None:
                        filedata = file.read()
                        file.close()
                    base64data = base64.b64encode(filedata)
                    czfiledata = b'PYCCX' + pswdata + zlib.compress(base64data, cz_level)
                    czfileobj = open(filepath + filename + '.pyccx', 'wb')
                    if czfileobj is not None:
                        czfileobj.write(czfiledata)
                        czfileobj.close()
                except FileNotFoundError:
                    notfound = True
                if notfound:
                    raise FileNotFound('{0}.pyc was not found.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to compress {0}.pyccx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to compress a python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to compress a python Bytecode file.')


def decompress_script(filepath, filename):
    """
    Decompresses a Python Script.
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            filedata = None
            try:
                file = io.open(filepath + filename + '.pycx', "rb")
                if file is not None:
                    filedata = file.read()
                    filedata = filedata[len(b'PYCX'):].strip()
                    file.close()
                if filedata.startswith(b'&pw='):
                    raise PasswordProtectedError(
                        'Cannot Decompress {0}.pycx due to Password Protection on the file.'.format(filename))
                else:
                    try:
                        decczfiledata = zlib.decompress(filedata)
                        base64decodeddata = base64.b64decode(decczfiledata)
                        decczfileobj = open(filepath + filename + '.py', 'wb')
                        if decczfileobj is not None:
                            decczfileobj.write(base64decodeddata)
                            decczfileobj.close()
                    except zlib.error as ex:
                        raise DecompressionError(str(ex))
            except FileNotFoundError:
                notfound = True
            if notfound:
                raise FileNotFound('{0}.pycx was not found.'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python script file.')


def decompress_protected_script(filepath, filename, password=None):
    """
    Same as decompress_script() but is for Decompressing password Protected pycx files.

    Password must be a byte string. This Function will then check and see if the byte string
    is in the file (in a compressed form ofc).
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :param password: byte string.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = base64.b64encode(password)
                filedata = None
                try:
                    file = io.open(filepath + filename + '.pycx', "rb")
                    if file is not None:
                        filedata = file.read()
                        filedata = filedata[len(b'PYCX'):].strip()
                        file.close()
                    if filedata.startswith(b'&pw='):
                        filedata = filedata[len(b'&pw='):].strip()
                        if filedata.startswith(pswdata):
                            filedata = filedata.strip(pswdata)
                            try:
                                decczfiledata = zlib.decompress(filedata)
                                base64decodeddata = base64.b64decode(decczfiledata)
                                decczfileobj = open(filepath + filename + '.py', 'wb')
                                if decczfileobj is not None:
                                    decczfileobj.write(base64decodeddata)
                                    decczfileobj.close()
                            except zlib.error as ex:
                                raise DecompressionError(str(ex))
                        else:
                            raise InvalidPassword('The Password Provided is Incorrect.')
                    else:
                        raise NoPasswordPresent('The file {0}.pycx is not Password Protected.'.format(filename))
                except FileNotFoundError:
                    notfound = True
                if notfound:
                    raise FileNotFound('{0}.pycx was not found.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to decompress {0}.pycx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python script file.')


def decompress_bytecode(filepath, filename):
    """
    Decompresses a Python Script.
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            filedata = None
            try:
                file = io.open(filepath + filename + '.pyccx', "rb")
                if file is not None:
                    filedata = file.read()
                    filedata = filedata[len(b'PYCCX'):].strip()
                    file.close()
                if filedata.startswith(b'&pw='):
                    raise PasswordProtectedError(
                        'Cannot Decompress {0}.pyccx due to Password Protection on the file.'.format(filename))
                else:
                    try:
                        decczfiledata = zlib.decompress(filedata)
                        base64decodeddata = base64.b64decode(decczfiledata)
                        decczfileobj = open(filepath + filename + '.pyc', 'wb')
                        if decczfileobj is not None:
                            decczfileobj.write(base64decodeddata)
                            decczfileobj.close()
                    except zlib.error as ex:
                        raise DecompressionError(str(ex))
            except FileNotFoundError:
                notfound = True
            if notfound:
                raise FileNotFound('{0}.pyccx was not found.'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python Bytecode file.')


def decompress_protected_bytecode(filepath, filename, password=None):
    """
    Same as decompress_bytecode() but is for Decompressing password Protected pycx files.

    Password must be a byte string. This Function will then check and see if the byte string
    is in the file (in a compressed form ofc).
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :param password: byte string.
    :return: None
    """
    notfound = False
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = base64.b64encode(password)
                filedata = None
                try:
                    file = io.open(filepath + filename + '.pyccx', "rb")
                    if file is not None:
                        filedata = file.read()
                        filedata = filedata[len(b'PYCCX'):].strip()
                        file.close()
                    if filedata.startswith(b'&pw='):
                        filedata = filedata[len(b'&pw='):].strip()
                        if filedata.startswith(pswdata):
                            filedata = filedata.strip(pswdata)
                            try:
                                decczfiledata = zlib.decompress(filedata)
                                base64decodeddata = base64.b64decode(decczfiledata)
                                decczfileobj = open(filepath + filename + '.pyc', 'wb')
                                if decczfileobj is not None:
                                    decczfileobj.write(base64decodeddata)
                                    decczfileobj.close()
                            except zlib.error as ex:
                                raise DecompressionError(str(ex))
                        else:
                            raise InvalidPassword('The Password Provided is Incorrect.')
                    else:
                        raise NoPasswordPresent('The file {0}.pyccx is not Password Protected.'.format(filename))
                except FileNotFoundError:
                    notfound = True
                if notfound:
                    raise FileNotFound('{0}.pyccx was not found.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to decompress {0}.pyccx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python Bytecode file.')


def this_is_not_a_function_to_keep_this_coment_in_byte_codes():
    """
    I would like for the data returned from this to be importable without  having to cache (only if
    sys.dont_write_bytecode is True) and without having to generate the normal py file as well.
    Why do this? what is the point?
    The Point for this is to make a interface to make python scripts smaller.
    With a range of 1/3 ~ 1/2 (results vary from file to file) the original sizes this is a dam good api for that.
    the cool thing is it uses python modules that comes with it. No External libs. (yet)
    Sadly this means somehow either recoding the original import statement in probably the C code to python itself.
    or finding how it reads from the pyc files (hopefully from within a python script).
    __init__.py:
        Normal Size: 568 bytes
        Compressed Size: 498 bytes
    api.py (this file):
        Normal Size: 25296 bytes
        Compressed Size: 5570 bytes
        PYCCX Compressed Size: 4163 bytes
    """
    pass


def dec_script(filepath, filename):
    """
    A Version of decompress_script() that does not write a Decompressed file. Instead it returns the bytes of the
    decompressed data.

    This is useful for when you want to import a pycx file that does not have a decompressed copy of itself.

    This also makes it possible for the python interpreter to write bytecode for it as well if sys.dont_write_bytecode
    is not set to True.

    The pro about this is the file name is required minus the '.pycx' part.

    Another benefit of this is that it can reduce a py file's size down by 1/3 (sometimes more) because of the
    base64 -> zlib compreesed data.

    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :return: File Bytes to decompressed file data. (no joke it returns bytes, not text, bytes!!!)
    """
    if filepath is not None:
        if filename is not None:
            filedata = None
            file = io.open(filepath + filename + '.pycx', "rb")
            if file is not None:
                filedata = file.read()
                filedata = filedata.strip(b'PYCX')
                file.close()
            try:
                decczfiledata = zlib.decompress(filedata)
                base64decodeddata = base64.b64decode(decczfiledata)
                return base64decodeddata
            except zlib.error as ex:
                raise DecompressionError(str(ex))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python script file.')


def dec_protected_script(filepath, filename, password=None):
    """
    A Version of dec_script() that Allows Decoding of Password Protected pycx files to byte data.
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :param password: Password (in bytes) to the file to decode to byte data.
    :return: File Bytes to decompressed file data. (no joke it returns bytes, not text, bytes!!!)
    """
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = base64.b64encode(password)
                filedata = None
                file = io.open(filepath + filename + '.pycx', "rb")
                if file is not None:
                    filedata = file.read()
                    filedata = filedata[len(b'PYCX'):].strip()
                    file.close()
                if filedata.startswith(b'&pw='):
                    filedata = filedata[len(b'&pw='):].strip()
                    if filedata.startswith(pswdata):
                        filedata = filedata[len(pswdata):].strip()
                        try:
                            decczfiledata = zlib.decompress(filedata)
                            base64decodeddata = base64.b64decode(decczfiledata)
                            return base64decodeddata
                        except zlib.error as ex:
                            raise DecompressionError(str(ex))
                    else:
                        raise InvalidPassword('The Password Provided is Incorrect.')
                else:
                    raise NoPasswordPresent('The file {0}.pycx is not Password Protected.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to decompress {0}.pycx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python script file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python script file.')


def dec_bytecode(filepath, filename):
    """
    A Version of decompress_bytecode() that does not write a Decompressed file. Instead it returns the bytes of the
    decompressed data.

    This is useful for when you want to import a pyccx file that does not have a decompressed copy of itself.

    The pro about this is the file name is required minus the '.pyccx' part.

    Another benefit of this is that it can reduce a pyc file's size down by 1/3 (sometimes more) because of the
    base64 -> zlib compressed data.

    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :return: File Bytes to decompressed file data. (no joke it returns bytes, not text, bytes!!!)
    """
    if filepath is not None:
        if filename is not None:
            filedata = None
            file = io.open(filepath + filename + '.pyccx', "rb")
            if file is not None:
                filedata = file.read()
                filedata = filedata.strip(b'PYCCX')
                file.close()
            try:
                decczfiledata = zlib.decompress(filedata)
                base64decodeddata = base64.b64decode(decczfiledata)
                return base64decodeddata
            except zlib.error as ex:
                raise DecompressionError(str(ex))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python Bytecode file.')


def dec_protected_bytecode(filepath, filename, password=None):
    """
    A Version of dec_bytecode() that Allows Decoding of Password Protected pycx files to byte data.
    :param filepath: Path to the file to decompress.
    :param filename: File name to decompress.
    :param password: Password (in bytes) to the file to decode to byte data.
    :return: File Bytes to decompressed file data. (no joke it returns bytes, not text, bytes!!!)
    """
    if filepath is not None:
        if filename is not None:
            if password is not None:
                pswdata = base64.b64encode(password)
                filedata = None
                file = io.open(filepath + filename + '.pyccx', "rb")
                if file is not None:
                    filedata = file.read()
                    filedata = filedata[len(b'PYCCX'):].strip()
                    file.close()
                if filedata.startswith(b'&pw='):
                    filedata = filedata[len(b'&pw='):].strip()
                    if filedata.startswith(pswdata):
                        filedata = filedata[len(pswdata):].strip()
                        try:
                            decczfiledata = zlib.decompress(filedata)
                            base64decodeddata = base64.b64decode(decczfiledata)
                            return base64decodeddata
                        except zlib.error as ex:
                            raise DecompressionError(str(ex))
                    else:
                        raise InvalidPassword('The Password Provided is Incorrect.')
                else:
                    raise NoPasswordPresent('The file {0}.pyccx is not Password Protected.'.format(filename))
            else:
                raise NoPasswordSpecified('A Password was not specified to decompress {0}.pyccx'.format(filename))
        else:
            raise FileNameNotProvided('A File Name was not provided to decompress a compressed python Bytecode file.')
    else:
        raise FilePathNotProvided('A File Path was not provided to decompress a compressed python Bytecode file.')