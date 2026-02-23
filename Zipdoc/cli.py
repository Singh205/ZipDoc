import argparse
import os
from zipdoc.optimizer import compress_text, open_file


def main():
    parser = argparse.ArgumentParser(prog="zipdoc")
    parser.add_argument("filepath")
    parser.add_argument("--open", action="store_true")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print("File not found")
        return

    if args.open:
        open_file(args.filepath)
        return

    old, new = compress_text(args.filepath)

    print("Compressed")
    print("Old:", old)
    print("New:", new)
    print("Saved:", old - new)