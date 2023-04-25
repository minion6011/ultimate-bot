@echo off
color f0



:MENU
title Minions Bot 4.0
cls
mode 86,30
echo.
echo.
echo                       ******* Minions dev bot *******
echo.
echo.
echo.
echo     A. Avvia                  B. Updater                            
echo.
echo.                              E. Tema scuro               F. Tema chiaro
echo.
echo.                              G. Setup                    
echo.

choice /c ABCDEFGHIJKLMNOPQRSTUVWXYZ /n /m "SELEZIONA DA ELENCO: "
cls
echo.
if %errorlevel%==1 goto A
if %errorlevel%==2 goto B
if %errorlevel%==3 goto C
if %errorlevel%==4 goto D
if %errorlevel%==5 goto E
if %errorlevel%==6 goto F
if %errorlevel%==7 goto G
if %errorlevel%==8 goto H
if %errorlevel%==9 goto I
if %errorlevel%==10 goto J
if %errorlevel%==11 goto K
if %errorlevel%==12 goto L
if %errorlevel%==13 goto M
if %errorlevel%==14 goto N
if %errorlevel%==15 goto O
if %errorlevel%==16 goto P
if %errorlevel%==17 goto Q
if %errorlevel%==18 goto R
if %errorlevel%==19 goto S
if %errorlevel%==20 goto T
if %errorlevel%==21 goto U
if %errorlevel%==22 goto V
if %errorlevel%==23 goto W
if %errorlevel%==24 goto X
if %errorlevel%==25 goto Y
if %errorlevel%==26 goto Z
if %errorlevel%==27 goto 1


::###########################################################  A 

:A
cls
py -3 main.py
echo.
echo Si e verificato un errore premere un tasto per continuare
pause >nul

::###########################################################  B

:B
py -3 updater.py
echo.
pause
cls
goto menu

::###########################################################  C

:C
goto menu

::###########################################################  D

:D
goto menu

::###########################################################  E

:E
color 0f
goto menu

::###########################################################  F

:F
color f0
goto menu

::###########################################################  G

:G
cls
py -3 -m pip install -U pip
py -3 -m pip install -U --user -r requirements.txt
pause
goto menu

::###########################################################  H

:H
goto menu

::###########################################################  I

:I

goto menu

::###########################################################  J

:J

goto menu

::###########################################################  K

:K

goto menu

::###########################################################  L

:L

goto menu

::###########################################################  M

:M

goto menu

::###########################################################  N 

:N

goto menu

::###########################################################  O

:O

goto menu

::###########################################################  P

:P

goto menu

::###########################################################  Q

:Q

goto menu

::###########################################################  R

:R

goto menu


::###########################################################  S

:S

goto menu

::###########################################################  T

:T

goto menu

::###########################################################  U

:U

goto menu

::###########################################################  V

:V

goto menu

::###########################################################  W

:W

goto menu

::###########################################################  X

:X

goto menu

::###########################################################  Y

:Y

goto menu

::###########################################################  Z

:Z

goto menu
::###########################################################
pause >nul





