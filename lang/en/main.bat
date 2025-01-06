@echo off
cd /d "%~dp0"
python libraries.py
cls
echo ========================================================================
echo ^;"								 	";
echo ^;"	__   __          _         _                             	";
echo ^;"	\ \ / /__  _   _| |_ _   _| |__   ___                    	";
echo ^;"	 \ V / _ \| | | | __| | | | '_ \ / _ \                   	";
echo ^;"	  | | (_) | |_| | |_| |_| | |_) |  __/                   	";
echo ^;"	  |_|\___/ \__,_|\__|\__,_|_.__/ \___|       _           	";
echo ^;"	  __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 	";
echo ^;"	 / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|	";
echo ^;"	| (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   	";
echo ^;"	 \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   	";
echo ^;"									";
echo ^;"									";
echo ========================================================================

:: Display information and warnings
powershell -Command "Write-Host 'Made by TigerZylinder' -BackgroundColor White -ForegroundColor Black"
powershell -Command "Write-Host 'This program uses yt-dlp and ffmpeg for downloading and converting videos.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'Please use this program cautiously, as you are responsible for all' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'downloaded content and its usage.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'By proceeding, you accept all consequences of this use.' -BackgroundColor Yellow -ForegroundColor Red"

:: Wait before starting the program
pause

:: Program information and start
powershell -Command "Write-Host 'Program is starting ...' -ForegroundColor Green"
python main.py
powershell -Command "Write-Host 'Program has ended' -ForegroundColor Red"

:: Another pause in case the user wants to see the completion message
pause