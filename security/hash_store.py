file_hashes = {}

def store_hash(file_path, hash_value):
    file_hashes[file_path] = hash_value

def get_hash(file_path):
    return file_hashes.get(file_path)

def remove_hash(file_path):
    if file_path in file_hashes:
        del file_hashes[file_path]