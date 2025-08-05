import time
import os
import psutil

# Script Monitor Settings
MONITOR_INTERVAL = 10  # seconds
SCRIPT_PATH = '/path/to/your/script.sh'  # path to your automation script

def is_script_running(script_path):
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if script_path in proc.info['cmdline']:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def monitor_script():
    while True:
        if is_script_running(SCRIPT_PATH):
            print(f"Script '{SCRIPT_PATH}' is running.")
        else:
            print(f"Script '{SCRIPT_PATH}' is not running.")
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    monitor_script()