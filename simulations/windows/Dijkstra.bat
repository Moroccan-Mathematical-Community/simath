@echo off
rem Launcher for Dijkstra simulation on Windows
set PYTHON=python
rem Resolve this script directory and call the Python module
set SCRIPT_DIR=%~dp0
set ALGO_DIR=%SCRIPT_DIR%..\..\algorithms\Dijkstra
%PYTHON% "%ALGO_DIR%\Dijkstra.py"
