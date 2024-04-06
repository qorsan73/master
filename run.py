import os
import sys
import time
os.system("pip install watchdog")
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("Code modified! Stopping execution.")
        sys.exit()

def monitor_code_changes(filename):
    event_handler = CodeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    filename_to_monitor = "cam.py"  # Replace with your actual filename
    monitor_code_changes(filename_to_monitor)
