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

:: Informationen und Warnungen anzeigen
powershell -Command "Write-Host 'Made by TigerZylinder' -BackgroundColor White -ForegroundColor Black"
powershell -Command "Write-Host 'Das Programm benutzt yt-dlp und ffmpeg zum Download und Konvertieren der Videos' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'Bitte benutze dieses Programm mit Vorsicht, da du fuer alle' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'heruntergeladenen Inhalte und deren Verwendung verantwortlich bist.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'Indem du fortfaehrst, akzeptierst du alle Konsequenzen dieser Nutzung.' -BackgroundColor Yellow -ForegroundColor Red"

:: Warten bevor das Programm startet
pause

:: Programmhinweis und Start
powershell -Command "Write-Host 'Programm wird gestartet ...' -ForegroundColor Green"
python main.py
powershell -Command "Write-Host 'Programm wurde beendet' -ForegroundColor Red"
:: Eine weitere Pause, falls der Benutzer den Abschluss sehen möchte
pause
