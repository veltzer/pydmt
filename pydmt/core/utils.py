import hashlib


def hex_digest(filename: str, algorithm_name: str) -> str:
    block_size = 65536
    hash_object = hashlib.new(algorithm_name)
    with open(filename, 'rb') as file_handle:
        buf = file_handle.read(block_size)
        while len(buf) > 0:
            hash_object.update(buf)
            buf = file_handle.read(block_size)
    return hash_object.hexdigest()


def sha1_file(filename: str) -> str:
    return hex_digest(filename, "sha1")
