#!/bin/bash

echo "Installing dependencies..."
/c/Python312/python.exe -m pip install -r requirements.txt # specify your windows python

echo "Running the game..."
/c/Python312/python.exe Platformer/Engine/main.py # specify your windows python
