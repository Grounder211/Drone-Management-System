@echo off

REM Server URL (change IP or hostname as needed)
set SERVER_URL=http://localhost:8000

REM File to download from the server
set FILE_NAME=modified.zip

REM Where to save downloaded files
set DOWNLOAD_DIR=C:\\Users\\ebalnee\\OneDrive - Ericsson\\Desktop\\test

REM Where to unzip files
set UNZIP_DIR=C:\\Users\\ebalnee\\OneDrive - Ericsson\\Desktop\\test

REM Create directories if not exist
if not exist "%DOWNLOAD_DIR%" mkdir "%DOWNLOAD_DIR%"
if not exist "%UNZIP_DIR%" mkdir "%UNZIP_DIR%"

REM Download file
echo Downloading %FILE_NAME% from %SERVER_URL%
curl -o "%DOWNLOAD_DIR%\%FILE_NAME%" "%SERVER_URL%/%FILE_NAME%"

REM Check if download succeeded
if errorlevel 1 (
    echo Download failed!
    exit /b 1
)

REM Unzip the file
echo Extracting %FILE_NAME%
powershell -Command "Expand-Archive -Path '%DOWNLOAD_DIR%\%FILE_NAME%' -DestinationPath '%UNZIP_DIR%' -Force"

REM Run test script if present
if exist "%UNZIP_DIR%\run_test.bat" (
    echo Running test script...
    call "%UNZIP_DIR%\run_test.bat"
) else (
    echo No test script found to run.
)

REM Clean up
echo Cleaning up...
del "%DOWNLOAD_DIR%\%FILE_NAME%"
rd /s /q "%UNZIP_DIR%"

echo Done.
pause
