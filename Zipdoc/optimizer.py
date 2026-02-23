import os
import gzip
import subprocess
import tempfile
from tqdm import tqdm
from zipdoc.huffman import huffman_compress, huffman_decompress

HEADER = b"ZDOC"


def compress_text(path):
    
    with open(path, "rb") as f:
        if f.read(4) == HEADER:
            print("File is already compressed.")
            return os.path.getsize(path), os.path.getsize(path)
    original_size = os.path.getsize(path)

    # gzip
    gzip_temp = path + ".gz"
    with open(path, "rb") as f_in, gzip.open(gzip_temp, "wb", compresslevel=9) as f_out:
        f_out.write(f_in.read())

    gzip_size = os.path.getsize(gzip_temp)

    # huffman
    huff_temp = path + ".huff"
    huffman_compress(path, huff_temp)
    huff_size = os.path.getsize(huff_temp)

    if min(gzip_size, huff_size) >= original_size:
        print("Compression not efficient. Keeping original file.")
        os.remove(gzip_temp)
        os.remove(huff_temp)
        return original_size, original_size

    if gzip_size < huff_size:
        method = b"G"
        best = gzip_temp
    else:
        method = b"H"
        best = huff_temp

    with open(best, "rb") as f:
        data = f.read()

    with open(path, "wb") as f:
        f.write(HEADER + method + data)

    os.remove(gzip_temp)
    os.remove(huff_temp)

    return original_size, os.path.getsize(path)


def open_file(path):
    with open(path, "rb") as f:
        header = f.read(4)
        if header != HEADER:
            os.startfile(path)
            return

        method = f.read(1)
        data = f.read()

    temp = tempfile.NamedTemporaryFile(delete=False)
    temp_path = temp.name

    if method == b"G":
        temp_gz = temp_path + ".gz"
        with open(temp_gz, "wb") as f:
            f.write(data)

        with gzip.open(temp_gz, "rb") as f:
            content = f.read()

        with open(temp_path, "wb") as f:
            f.write(content)

        os.remove(temp_gz)

    elif method == b"H":
        temp_huff = temp_path + ".huff"
        with open(temp_huff, "wb") as f:
            f.write(data)

        huffman_decompress(temp_huff, temp_path)
        os.remove(temp_huff)

    os.startfile(temp_path)