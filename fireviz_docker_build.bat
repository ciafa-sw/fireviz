@echo off
title FIREVIZ_BUILD
:loop
echo.
echo.
echo.
echo Building Docker image...
docker build -f C:\Users\dasilva\Documents\firefront\fireviz\fireviz.Dockerfile -t ciafa:fireviz C:\Users\dasilva\Documents\firefront\fireviz\

echo Shutdown...
