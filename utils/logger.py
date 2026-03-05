import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "activity.log")

# Ensure logs directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_event(action, src, dest=None):

    if dest:
        logging.info(f"{action} | Source: {src} | Destination: {dest}")
    else:
        logging.info(f"{action} | Source: {src}")
