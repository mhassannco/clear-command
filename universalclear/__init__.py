__version__ = '0.1'

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
