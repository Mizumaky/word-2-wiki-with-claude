@echo off
:: Word2Wiki Launcher - Double-click to start the conversion tool
:: This batch file launches the Python-based Word to Wiki converter

title Word2Wiki Converter
color 0A

:: Change to the directory containing this batch file
cd /d "%~dp0"

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from: https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

:: Check if requirements are installed
python -c "import click, pypandoc, rich, bs4, questionary" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing required dependencies...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo Failed to install dependencies
        echo.
        pause
        exit /b 1
    )
)

:: Launch the interactive Python launcher
python interactive_launcher.py

:: Keep window open on exit
pause