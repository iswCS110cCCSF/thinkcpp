@echo off
cd /d "%~dp0"

pretext build web

if errorlevel 1 (
    echo.
    echo Build failed. The custom CSS was not applied.
    pause
    exit /b 1
)

type "%~dp0custom-toc.css" >> "%~dp0output\output\html\_static\pretext\css\theme.css"

echo.
echo Build completed with custom TOC symbols.
pretext view web
