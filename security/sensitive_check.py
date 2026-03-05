import os
from config import SENSITIVE_DIRS

def is_sensitive(file_path):
    if not file_path:
        return False

    file_path = os.path.normpath(file_path)

    for directory in SENSITIVE_DIRS:
        directory = os.path.normpath(directory)
        if file_path.startswith(directory):
            return True

    return False
