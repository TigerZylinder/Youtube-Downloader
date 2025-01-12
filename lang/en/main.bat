@echo off
:: Ensure that the script starts in the current directory
cd /d "%~dp0"
:: Clear the screen
cls

:: Display banner
echo ===============================================================
echo ^;"                                                             ";
echo ^;"   __   __          _         _                              ";
echo ^;"   \ \ / /__  _   _| |_ _   _| |__   ___                     ";
echo ^;"    \ V / _ \| | | | __| | | | '_ \ / _ \                    ";
echo ^;"     | | (_) | |_| | |_| |_| | |_) |  __/                    ";
echo ^;"     |_|\___/ \__,_|\__|\__,_|_.__/ \___|       _            ";
echo ^;"     __| | _____      ___ __ | | ___   __ _  __| | ___ _ __  ";
echo ^;"    / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__| ";
echo ^;"   | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |    ";
echo ^;"    \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|    ";
echo ^;"                                                             ";
echo ^;"                                                             ";
echo ===============================================================

:: Display warnings and information
powershell -Command "Write-Host 'Created by TigerZylinder' -BackgroundColor White -ForegroundColor Black"
powershell -Command "Write-Host 'This program uses yt-dlp and ffmpeg to download and convert videos.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "$OutputEncoding = New-Object -typename System.Text.UTF8Encoding; Write-Host 'Please use this program responsibly. You are responsible for all' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'downloaded content and its usage.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'By continuing, you accept all consequences of using this program.' -BackgroundColor Yellow -ForegroundColor Red"
pause
:: Start main program
powershell -Command "Write-Host 'The program is starting...' -ForegroundColor Green"
python main.py
powershell -Command "Write-Host 'The program has finished.' -ForegroundColor Red"

:: Define log file
set LOGFILE=log.txt

:: Redirect CMD output to the log file
(
    echo ================================
    echo Start time: %date% %time%
    echo ================================
    echo.
    echo Info:
    :: You can add your desired commands here
    python --version
    echo Finished: %date% %time%
) >> %LOGFILE% 2>&1

:: Pause to allow the user to check the completion
pause
