import hashlib

salt = bytes("stpx1!#s0f8p6v5sdq", "UTF-8")


def signature_generate(original_bytes: bytes) -> str:
    combined_array = bytearray()
    combined_array.extend(original_bytes)
    combined_array.extend(salt)
    value = hashlib.md5(combined_array)
    return value.hexdigest()
