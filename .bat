@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Running the game...

python Platformer\Engine\main.py
