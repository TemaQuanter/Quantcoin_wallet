from hash_calculater import get_hash

def get_string_from_binary_file(path):
    binary_content = None
    with open(path, 'rb') as file:
        binary_content = file.read(-1)
    return str(binary_content)

def get_nft_hash_from_binary_file(path):
    return get_hash(get_string_from_binary_file(path))