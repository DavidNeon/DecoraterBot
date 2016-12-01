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
from importlib.machinery import FileFinder
import zlib
import json
import base64
import sys
from ._pycx_backend import *


class JsonImporter(ExtensionImporter):
    """JSON File Importer Class."""
    def __init__(self):
        super(JsonImporter, self).__init__(['.json'])

    def load_module(self, fullname):
        """Loads modules found with the extension"""
        premodule = super(JsonImporter, self).load_module(fullname)
        if premodule is None:
            try:
                with open(self.path) as f:
                    module = json.load(f)
                    sys.modules[fullname] = module
                    return module
            except FileNotFoundError:
                raise ImportError('Could not import the json file {0}'.format(fullname))


class PycxImporter(ExtensionImporter):
    """PYCX File Importer Class."""
    def __init__(self):
        super(PycxImporter, self).__init__(['.pycx'])

    def load_module(self, fullname):
        """
        Loads modules found with the pycx excention.

        Info: pycx files are compressed python source code files.

        Order of processing (to import):
            zlib decompression
            base64 decode.
        """
        premodule = super(PycxImporter, self).load_module(fullname)
        if premodule is None:
            try:
                with open(self.path, 'rb') as f:
                    filedata = f[len(b'PYCX'):].strip()
                    try:
                        decczfiledata = zlib.decompress(filedata)
                        decoded_data = base64.b64decode(decczfiledata)
                    except zlib.error as ex:
                        raise ImportError('Could not import {0} because of exception:\n{1}.'.format(fullname, str(ex)))
                    # assume utf8 encoding. utf8 is standard python script encoding anyways.
                    module = decoded_data.decode("utf-8")
                    sys.modules[fullname] = module
                    return module
            except FileNotFoundError:
                raise ImportError('Could not import {0}.'.format(fullname))


extension_importers = [JsonImporter(), PycxImporter()]
hook_list = []
for importer in extension_importers:
    hook_list.append((importer.find_loader, importer.extensions))

sys.path_hooks.insert(0, FileFinder.path_hook(*hook_list))
sys.path_importer_cache.clear()
