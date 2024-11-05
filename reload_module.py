import subprocess
import os

def reload():
    dir = os.getcwd()
    path = os.path.join(dir, 'reload.sh')
    if os.path.isfile(path):
        try:
            result = subprocess.run([path], check=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while reloading: {e}")
            print("Run start.py manually.") 
            print("\nExiting...") 
            sys.exit()
    else:
        print("reload.sh not found in the current directory.")

reload()