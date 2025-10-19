@echo off
REM ============================================
REM Google Maps Scraper - EXE Builder
REM Simple batch file alternative to PowerShell
REM ============================================

echo.
echo ============================================
echo   Google Maps Scraper - EXE Builder
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "env\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run setup.ps1 first:
    echo    .\setup.ps1
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/6] Activating virtual environment...
call env\Scripts\activate.bat

REM Install PyInstaller
echo [2/6] Installing PyInstaller...
pip install pyinstaller==6.11.1 --quiet

REM Clean previous builds
echo [3/6] Cleaning previous builds...
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build

REM Check for icon
echo [4/6] Checking for icon file...
if not exist "assets\icon.ico" (
    echo.
    echo [WARNING] Icon file not found: assets\icon.ico
    echo.
    echo Options:
    echo   1. Create icon: python create_icon.py
    echo   2. Continue without icon (uses default Python icon)
    echo   3. Cancel and add icon manually to assets\icon.ico
    echo.
    choice /c 123 /m "Choose option"
    if errorlevel 3 (
        echo.
        echo Build cancelled. Add your icon to assets\icon.ico
        pause
        exit /b 0
    )
    if errorlevel 2 goto BUILD
    if errorlevel 1 (
        echo.
        echo Creating default icon...
        pip install Pillow --quiet
        python create_icon.py
        if errorlevel 1 (
            echo.
            echo Failed to create icon. Building without icon...
        )
    )
)

:BUILD
REM Build executable
echo [5/6] Building executable...
echo.
pyinstaller build_exe.spec

REM Check if build succeeded
if not exist "dist\GoogleMapsScraper\GoogleMapsScraper.exe" (
    echo.
    echo ============================================
    echo [ERROR] Build failed!
    echo ============================================
    echo.
    echo Check the output above for errors.
    echo Common issues:
    echo   - Missing dependencies: pip install -r requirements.txt
    echo   - Antivirus blocking: Add exception for project folder
    echo   - Disk space: Need at least 500 MB free
    echo.
    pause
    exit /b 1
)

REM Success!
echo.
echo ============================================
echo [SUCCESS] Build completed!
echo ============================================
echo.

REM Get file size
for %%A in ("dist\GoogleMapsScraper\GoogleMapsScraper.exe") do (
    set size=%%~zA
    set /a sizeMB=%%~zA/1048576
)

echo Output: dist\GoogleMapsScraper\GoogleMapsScraper.exe
echo Size: %sizeMB% MB
echo.
echo Next steps:
echo   1. Test the executable:
echo      cd dist\GoogleMapsScraper
echo      GoogleMapsScraper.exe
echo.
echo   2. Distribute the entire folder:
echo      dist\GoogleMapsScraper\
echo.
echo   3. Create ZIP for sharing:
echo      Right-click dist\GoogleMapsScraper
echo      Send to ^> Compressed folder
echo.

REM Deactivate virtual environment
call env\Scripts\deactivate.bat

pause
