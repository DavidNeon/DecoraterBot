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
        options, arguments = getopt.getopt(argv, 'p:f:a:', ['path=', 'filename=', 'password='])
    except getopt.GetoptError:
        sys.exit(2)
    in_path = None
    filename = None
    pswd = None
    for option, argument in options:
        if option in ('p', '--path'):
            in_path = argument
        if option in ('f', '--filename'):
            filename = argument
        if option in ('a', '--password'):
            pswd = argument
    if filename is not None:
        if pswd is not None:
            try:
                api.decompress_protected_bytecode(in_path, filename + "." + sys.implementation.cache_tag, password=pswd)
                print('Password Protected Bytecode Decompression Complete.')
            except api.InvalidPassword as err:
                print('Error: {0}'.format(str(err)))
            except api.NoPasswordPresent as err:
                print('Error: {0}'.format(str(err)))
            except api.FileNotFound as err:
                print('Error: {0}'.format(str(err)))
            except api.NoPasswordSpecified as err:
                print('Error: {0}'.format(str(err)))
            except api.FilePathNotProvided as err:
                print('Error: {0}'.format(str(err)))
            except api.FileNameNotProvided as err:
                print('Error: {0}'.format(str(err)))
            except api.DecompressionError as err:
                print('Error: {0}'.format(str(err)))
        else:
            try:
                api.decompress_bytecode(in_path, filename + "." + sys.implementation.cache_tag)
                print('Bytecode Decompression Complete.')
            except api.FileNotFound as err:
                print('Error: {0}'.format(str(err)))
            except api.PasswordProtectedError as err:
                print('Error: {0}'.format(str(err)))
            except api.FilePathNotProvided as err:
                print('Error: {0}'.format(str(err)))
            except api.FileNameNotProvided as err:
                print('Error: {0}'.format(str(err)))
            except api.DecompressionError as err:
                print('Error: {0}'.format(str(err)))
    else:
        print('Error: A File Name was not provided to decompress a python Bytecode file.')

if __name__ == "__main__":
    main(sys.argv[1:])
