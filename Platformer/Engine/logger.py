# logger.py

import os
from datetime import datetime

'''The module to log'''

def setup():
    global log_file_location
    log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.platformer', 'Logs'))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file_location = os.path.abspath(os.path.join(log_dir, f'log.log'))

def log(messege: str) -> None:
    '''Log the messege to the file'''
    with open(log_file_location, 'a') as file_log:
        print(f'{messege} at _{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}', file=file_log)
        print(messege)