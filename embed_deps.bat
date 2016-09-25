@echo off
"%~dp0\resources\python35x64\win32\python.exe" "%~dp0\zipmaker\make_zip.py" -b "%~dp0\resources\python35\win32" -s "%~dp0\zipmaker\deps" -e -o "%~dp0\zipmaker\DecoraterBot-deps"
pause