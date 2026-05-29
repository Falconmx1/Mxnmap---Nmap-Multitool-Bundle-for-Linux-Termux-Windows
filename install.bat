@echo off
title Instalador Mxnmap
echo ===================================
echo    Instalando Mxnmap para Windows
echo ===================================

:: Verificar si Nmap está instalado
where nmap >nul 2>nul
if %errorlevel% neq 0 (
    echo [*] Nmap no encontrado, descargando...
    powershell -Command "Invoke-WebRequest -Uri 'https://nmap.org/dist/nmap-7.95-setup.exe' -OutFile '%TEMP%\nmap-setup.exe'"
    start /wait %TEMP%\nmap-setup.exe /S
)

:: Crear carpeta Mxnmap en el perfil del usuario
mkdir "%USERPROFILE%\.mxnmap"
copy mxnmap.py "%USERPROFILE%\.mxnmap\"
copy config\banner.txt "%USERPROFILE%\.mxnmap\"

:: Crear un batch para ejecutar mxnmap desde CMD
echo @echo off > "%USERPROFILE%\.mxnmap\mxnmap.cmd"
echo python "%USERPROFILE%\.mxnmap\mxnmap.py" %%* >> "%USERPROFILE%\.mxnmap\mxnmap.cmd"

:: Agregar a PATH (opcional)
setx PATH "%PATH%;%USERPROFILE%\.mxnmap"

echo [✔] Instalación completada. Reinicia CMD y usa: mxnmap --help
pause
