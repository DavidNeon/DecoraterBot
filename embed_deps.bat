@echo off
"%SystemDrive%\python352\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.5.1
"H:\Python\Python351\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.5.0
"H:\Python\python350\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.4.5
"H:\Python\Python345\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.4.4
"H:\Python\Python344\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.4.3
"H:\Python\Python343\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
REM Now for local 3.4.2
"H:\Python\Python342\python.exe" "%~dp0\zipmaker\make_zip.py" -s "%~dp0\zipmaker\deps" -o "%~dp0\zipmaker\DecoraterBot-deps"
pause