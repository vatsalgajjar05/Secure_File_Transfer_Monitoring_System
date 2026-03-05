import os
from config import AUTHORIZED_DESTINATIONS

def is_authorized(destination):

    if not destination:
        return True

    destination = os.path.normpath(destination)

    for allowed in AUTHORIZED_DESTINATIONS:
        allowed = os.path.normpath(allowed)
        if destination.startswith(allowed):
            return True

    return False
