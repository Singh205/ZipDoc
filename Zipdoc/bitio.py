class BitWriter:
    def __init__(self, file):
        self.file = file
        self.buffer = 0
        self.nbits = 0

    def write_bits(self, bits):
        for bit in bits:
            self.buffer = (self.buffer << 1) | int(bit)
            self.nbits += 1

            if self.nbits == 8:
                self.file.write(bytes([self.buffer]))
                self.buffer = 0
                self.nbits = 0

    def flush(self):
        if self.nbits > 0:
            self.buffer <<= (8 - self.nbits)
            self.file.write(bytes([self.buffer]))
            self.buffer = 0
            self.nbits = 0


class BitReader:
    def __init__(self, file):
        self.file = file
        self.buffer = 0
        self.nbits = 0

    def read_bit(self):
        if self.nbits == 0:
            byte = self.file.read(1)
            if not byte:
                return None
            self.buffer = ord(byte)
            self.nbits = 8

        self.nbits -= 1
        return (self.buffer >> self.nbits) & 1