@echo off
REM Directory to serve files from:
set SERVE_DIR=C:\\Users\\ebalnee\\OneDrive - Ericsson\\Desktop\\test\\Drone-Management-System

REM Port to listen on:
set PORT=8000

REM Start the HTTP server
echo Starting HTTP server on port %PORT%, serving files from %SERVE_DIR%
python -m http.server %PORT% --directory "%SERVE_DIR%"
pause
