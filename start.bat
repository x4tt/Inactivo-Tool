@echo off
title INACTIVO-TOOL - Launcher
color 0A

echo Iniciando INACTIVO-TOOL...
echo ---------------------------

:: Esperar 1 segundo
timeout /t 1 > nul

:: Ejecutar el menú
python inactivo_tool.py

pause
