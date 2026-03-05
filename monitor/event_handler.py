import os
from watchdog.events import FileSystemEventHandler
from security.sensitive_check import is_sensitive
from security.hashing import calculate_hash
from security.authorization import is_authorized
from utils.logger import log_event
from security.hash_store import store_hash, get_hash, remove_hash
from config import DEBUG


class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        handle_event("CREATED", event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        handle_event("MODIFIED", event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        handle_event("DELETED", event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            return
        handle_event("MOVED", event.src_path, event.dest_path)


def handle_event(action, src, dest=None):

    if not src:
        return

    src = os.path.normpath(src)
    if dest:
        dest = os.path.normpath(dest)

    # ---------------- CREATED ----------------
    if action == "CREATED":

    # If file is created outside protected folder
        if not is_sensitive(src):
            print("ALERT: Unauthorized Movement Detected")
            log_event("Unauthorized Movement", src, dest)
            

        log_event(action, src, dest)
        return


    # ---------------- MODIFIED ----------------
    elif action == "MODIFIED":

        if not is_sensitive(src):
            log_event(action, src, dest)
            return

        try:
            new_hash = calculate_hash(src)
        except:
            return

        if not new_hash:
            return

        old_hash = get_hash(src)

        if old_hash is None:
            store_hash(src, new_hash)
            print("Baseline hash stored.")
            log_event(action, src, dest)
            return

        if new_hash != old_hash:
            print("ALERT: Hash Mismatch Detected (Possible Tampering)")
            log_event("Integrity Violation", src, dest)
            store_hash(src, new_hash)

        log_event(action, src, dest)
        return

    # ---------------- MOVED ----------------
    elif action == "MOVED":

        if DEBUG:
            print("DEBUG SRC:", src)
            print("DEBUG DEST:", dest)
            print("Is Sensitive:", is_sensitive(src))
            print("Is Authorized:", is_authorized(dest))

        # Rename handling (hash update)
        old_hash = get_hash(src)
        if old_hash and dest:
            store_hash(dest, old_hash)
            remove_hash(src)

        # Unauthorized move detection
        if is_sensitive(src) and dest and not is_authorized(dest):
            print("ALERT: Unauthorized Movement Detected")
            log_event("Unauthorized Movement", src, dest)

        log_event(action, src, dest)
        return

    # ---------------- DELETED ----------------
    elif action == "DELETED":

        if is_sensitive(src):
            print("ALERT: Sensitive File Removed From Protected Directory")
            log_event("Unauthorized Movement", src, dest)

        remove_hash(src)
        log_event(action, src, dest)
        return