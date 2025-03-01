#!/bin/bash

echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Running the game..."
python3 Platformer/Engine/main.py
