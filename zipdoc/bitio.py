def pad_encoded_text(encoded_text):
    extra_padding = 8 - (len(encoded_text) % 8)

    if extra_padding == 8:
        extra_padding = 0

    encoded_text += "0" * extra_padding

    padded_info = "{0:08b}".format(extra_padding)

    encoded_text = padded_info + encoded_text

    return encoded_text


def get_byte_array(padded_encoded_text):
    """
    Convert padded bit string into actual bytearray.
    """

    if len(padded_encoded_text) % 8 != 0:
        raise ValueError("Encoded text not properly padded")

    byte_array = bytearray()

    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        byte_array.append(int(byte, 2))

    return byte_array


def remove_padding(padded_encoded_text):
    """
    Remove padding after reading from file.
    """

    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)

    encoded_text = padded_encoded_text[8:]

    if extra_padding > 0:
        encoded_text = encoded_text[:-extra_padding]

    return encoded_text


def bytes_to_bitstring(byte_data):
    """
    Convert bytes back into bit string.
    """

    bit_string = ""

    for byte in byte_data:
        bit_string += "{0:08b}".format(byte)

    return bit_string
