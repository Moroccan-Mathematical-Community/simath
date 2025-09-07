@echo off
REM SierpinskiFractal simulation launcher for Windows
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%..\..\.."
python algorithms\SierpinskiFractal\SierpinskiFractal.py %*
