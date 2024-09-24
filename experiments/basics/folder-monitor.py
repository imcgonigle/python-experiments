import os
import time

def monitor_folder(path):
    previous = set(os.listdir(path))
    print(f"Monitoring changes in {path}. Press Ctrl+c to stop.")
    try:
        while True:
            time.sleep(2)
            current = set(os.listdir(path))
            added = current - previous
            removed = previous - current
            if added:
                print(f"Added: {', '.join(added)}")
            if removed:
                print(f"Removed: {', '.join(removed)}")
            previous = current
    except KeyboardInterrupt:
        print("Monitoring stopped")

if __name__ == "__main__":
    path = input("Enter folder path to monitor: ")
    monitor_folder(path)

