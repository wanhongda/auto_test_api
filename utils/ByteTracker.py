import binascii


class ByteTracker(object):
    # the message we keep
    message: bytearray
    index: int
    order_rule: str

    def __init__(self, rule: str):
        self.index = 0
        self.message = bytearray()
        self.order_rule = rule

    def put(self, source_bytes: bytes):
        self.message.extend(source_bytes)
        self.index += len(source_bytes)

    def put_int(self, value: int):
        self.put(value.to_bytes(4, self.order_rule))

    def put_long(self, value: int):
        self.put(value.to_bytes(8, self.order_rule))

    def put_string(self, text: str, length: int = 0):

        text_bytes = bytes(text, "UTF-8")

        if length == 0:
            length = len(text_bytes)
            # append a int for dynamic string bytes length
            self.put_int(length)

        target = bytearray(length)
        min_len = min(length, len(text_bytes))
        index = 0
        while index < min_len:
            target[index] = text_bytes[index]
            index += 1
        self.put(target)

    def get(self, length: int) -> bytes:
        remained_bytes_len = len(self.message) - self.index
        if remained_bytes_len < length:
            raise ValueError('没有足够长度的字节')
        value = self.message[self.index:self.index + length]
        self.index += length

        return value

    def get_int(self) -> int:
        return int.from_bytes(self.get(4), self.order_rule)

    def get_long(self) -> int:
        return int.from_bytes(self.get(8), self.order_rule)

    def get_string(self, length=-1) -> str:
        # this means you should get from byte_tracker
        if length == -1:
            length = self.get_int()

        if length == 0:
            return ""
        original_bytes = self.get(length)

        # EOF handle
        handled_bytes = bytearray()
        for byte in original_bytes:
            # EOF happened
            if byte == 0:
                break
            else:
                handled_bytes.append(byte)

        if len(handled_bytes) == 0:
            return ""
        return str(handled_bytes, "UTF-8")

    def print(self) -> str:
        return str(binascii.b2a_base64(self.message), "UTF-8")

    def load(self, encoded_text: str):
        self.message.extend(binascii.a2b_base64(bytes(encoded_text, "UTF-8")))
