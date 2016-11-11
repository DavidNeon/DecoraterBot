"""
Generic zip file maker for compiling pyc files in.
"""
# TODO: Actually write zip files here.
import os

def compilefile(filepath, filename, fileext, directory):
    if os.path.exists(filepath):
        if not os.path.exists(directory):
            c = compile(open(filepath + filename + fileext), filename, 'exec')
            compiledfile = open(directory + filename + '.pyc', 'a')
            compiledfile.write(c)
