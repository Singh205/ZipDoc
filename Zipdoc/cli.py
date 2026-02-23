import argparse
import os
from zipdoc.optimizer import compress_text, compress_pdf, open_file


def main():
    parser = argparse.ArgumentParser(prog="zipdoc")
    parser.add_argument("filepath", help="Path to file")
    parser.add_argument("--open", action="store_true", help="Open file (auto-decompress if needed)")

    args = parser.parse_args()
    path = args.filepath

    if not os.path.exists(path):
        print("File not found.")
        return

    if args.open:
        open_file(path)
        return

    ext = path.split(".")[-1].lower()

    try:
        if ext == "txt":
            old, new = compress_text(path)
        elif ext == "pdf":
            old, new = compress_pdf(path)
        else:
            print("Unsupported file type.")
            return

        print("\nCompression Complete")
        print("Old Size:", old)
        print("New Size:", new)
        print("Saved:", old - new)

    except Exception as e:
        print("Error:", e)