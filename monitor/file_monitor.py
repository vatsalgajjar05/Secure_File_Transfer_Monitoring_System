from watchdog.observers import Observer
from monitor.event_handler import MonitorHandler
import time

def start_monitoring():

    path = "C:/Intern_test"

    observer = Observer()
    observer.schedule(MonitorHandler(), path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
