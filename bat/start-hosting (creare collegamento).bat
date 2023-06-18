@echo off
:A
color 02
mode 86,30
py -3 updater.py
cls
py -3 -m pip install -U pip
py -3 -m pip install -U --user -r requirements.txt
py -3 -m pip install --upgrade -r requirements.txt

cls

py -3 main.py
echo.
echo Si e verificato un errore 20 s al riavvio
timeout /t 20
goto A
