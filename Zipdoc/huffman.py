import heapq
import os
import pickle
from collections import Counter
from tqdm import tqdm


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(data):
    freq = Counter(data)
    heap = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(root, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if root.char is not None:
        code_map[root.char] = prefix
        return

    build_codes(root.left, prefix + "0", code_map)
    build_codes(root.right, prefix + "1", code_map)
    return code_map


def huffman_compress(input_path, output_path):
    with open(input_path, "rb") as f:
        data = f.read()

    tree = build_tree(data)
    codes = build_codes(tree)

    encoded = "".join(codes[b] for b in data)

    padded = encoded + "0" * ((8 - len(encoded) % 8) % 8)

    byte_array = bytearray()
    for i in range(0, len(padded), 8):
        byte_array.append(int(padded[i:i+8], 2))

    with open(output_path, "wb") as f:
        pickle.dump(tree, f)
        f.write(byte_array)


def huffman_decompress(input_path, output_path):
    with open(input_path, "rb") as f:
        tree = pickle.load(f)
        bit_data = f.read()

    bits = "".join(f"{byte:08b}" for byte in bit_data)

    decoded = []
    node = tree
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded.append(node.char)
            node = tree

    with open(output_path, "wb") as f:
        f.write(bytes(decoded))