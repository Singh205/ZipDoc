from zipdoc.huffman import build_huffman_tree, generate_codes


def encode(data, codebook):
    """Convert original data into bit string using codebook"""
    encoded_output = ""
    for byte in data:
        encoded_output += codebook[byte]
    return encoded_output


def decode(encoded_data, root):
    """Decode bit string back to original data using Huffman tree"""
    decoded_output = ""
    current = root

    for bit in encoded_data:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.byte is not None:
            decoded_output += current.byte
            current = root 

    return decoded_output


def test_huffman():
    test_text = "aaabbc"

    print("Original Text:", test_text)
    root = build_huffman_tree(test_text)
    codebook = generate_codes(root)
    print("Generated Codes:", codebook)

    encoded = encode(test_text, codebook)
    print("Encoded Data:", encoded)

    decoded = decode(encoded, root)
    print("Decoded Data:", decoded)

    if decoded == test_text:
        print("SUCCESS: Huffman is working correctly")
    else:
        print("ERROR: Decoded text does not match original")


if __name__ == "__main__":
    test_huffman()
