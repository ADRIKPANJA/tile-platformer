# Run_Game.py

import subprocess
import os
import sys

'''Runs the game'''

print(f'Running on {os.name}')
if os.name == 'nt':
    if not 'MSYSTEM' in os.environ:
        subprocess.run(f'.bat', shell=True, cwd=os.path.abspath(os.path.dirname(__file__)))
    else:
        print("ON MSYS")
        subprocess.run(['bash', '-c', 'chmod +x msys.sh'], shell=True, cwd=os.path.abspath(os.path.dirname(__file__)))
        subprocess.run(['bash', '-c', './msys.sh'], shell=True, cwd=os.path.abspath(os.path.dirname(__file__)))

else:
    subprocess.run(['chmod +x .sh'], shell=True, cwd=os.path.abspath(os.path.dirname(__file__)))
    subprocess.run('./.sh', shell=True, cwd=os.path.abspath(os.path.dirname(__file__)))