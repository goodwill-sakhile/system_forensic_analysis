# Hash Utilities

import hashlib

def hash_file(file_path: str, algo: str = "sha256") -> str:
    hash_func = getattr(hashlib, algo)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()