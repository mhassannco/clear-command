# Universal Clear Command

A universal clear command!

Designed to help you have a universal clear command in your environment, long gone are the days of having to define 'cls' and 'clear' for each operating system. 
Now embrace change and use the newly released clear-command, which defines a UNIVERSAL clear command for all to use!

## Installation

Install via pip!
```bash
pip install clear-command
https://pypi.org/project/clear-command/


Devoloped by Malik Hassan with much love!

Example Code:

\\\
import time
from clear_command import clearCommand

def main():
    clear = clearCommand()
    print(f"Command to clear console: {command}")
    
    time.sleep(2.5)
    
    import os
    os.system(clear)

if __name__ == "__main__":
    main()
\\\

This script will print the command to clear your console, then wait 2.5 seconds and clear the console.
