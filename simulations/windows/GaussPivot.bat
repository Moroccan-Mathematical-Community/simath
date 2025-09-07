@echo off
REM GaussPivot simulation launcher for Windows
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%..\..\.."
python algorithms\GaussPivot\GaussPivot.py %*
