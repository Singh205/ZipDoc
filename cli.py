import argparse
from .compressor import compress
from .decompressor import decompress


def main():
    parser = argparse.ArgumentParser(description="ZipDoc CLI Compressor")

    parser.add_argument("mode", choices=["compress", "decompress"])
    parser.add_argument("file")

    args = parser.parse_args()

    if args.mode == "compress":
        compress(args.file)
    else:
        decompress(args.file)


if __name__ == "__main__":
    main()