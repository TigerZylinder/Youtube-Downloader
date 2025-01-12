@echo off
:: Sicherstellen, dass das Skript im aktuellen Verzeichnis gestartet wird
cd /d "%~dp0"
python libraries.py
cls

:: Banner anzeigen
echo  ===============================================================
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
echo  ===============================================================

:: Warnungen und Informationen anzeigen
powershell -Command "Write-Host 'Erstellt von TigerZylinder' -BackgroundColor White -ForegroundColor Black"
powershell -Command "Write-Host 'Dieses Programm nutzt yt-dlp und ffmpeg, um Videos herunterzuladen und zu konvertieren.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'Bitte benutze dieses Programm verantwortungsbewusst. Du bist fuer alle' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'heruntergeladenen Inhalte und deren Nutzung verantwortlich.' -BackgroundColor Red -ForegroundColor Yellow"
powershell -Command "Write-Host 'Indem du fortfaehrst, akzeptierst du alle Konsequenzen der Nutzung dieses Programms.' -BackgroundColor Yellow -ForegroundColor Red"
pause
:: Hauptprogramm starten
powershell -Command "Write-Host 'Das Programm startet...' -ForegroundColor Green"
python main.py
powershell -Command "Write-Host 'Das Programm wurde beendet.' -ForegroundColor Red"

:: Logdatei definieren
set LOGFILE=log.txt

:: CMD-Ausgabe in die Logdatei umleiten
(
    echo ================================
    echo Startzeit: %date% %time%
    echo ================================
    echo.
    echo Info:
    :: Hier können deine gewünschten Befehle hinzugefügt werden
    python --version
    echo Fertig: %date% %time%
) >> %LOGFILE% 2>&1

:: Pause, damit der Benutzer den Abschluss überprüfen kann
pause
