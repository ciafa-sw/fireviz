#!/bin/bash
echo "Killing and removing Docker container..."
docker kill fireviz
docker rm fireviz
echo "Starting Docker container..."
docker run --name fireviz -p 5000:5000 -v $(pwd):/fireviz --rm -it ciafa:fireviz
echo "Shutdown..."
