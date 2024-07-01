import time
from clear_command import clearCommand

def main():
    command = clearCommand()
    print(f"Command to clear console: {command}")
    time.sleep(2.5)
    # Assuming you want to actually clear the console
    import os
    os.system(command)

if __name__ == "__main__":
    main()
