@echo off
title FIREVIZ_DEV
:loop
echo.
echo.
echo.
echo Killing and removing Docker container...
docker kill fireviz
docker rm fireviz
echo Starting Docker container...
docker run -it ^
           --name fireviz ^
		   -p 5000:5000 ^
           -v C:\Users\dasilva\Documents\firefront:/fireviz ^
           ciafa:fireviz
echo Shutdown...
goto loop