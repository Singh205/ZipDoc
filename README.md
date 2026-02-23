# ZIPDOC

A smart CLI-based file compressor for Windows.

ZIPDOC compresses `.txt` files using Huffman coding and GZIP, automatically selecting the most efficient method.

It also supports `.pdf` compression using Ghostscript.

## Features

- Smart compression (Huffman vs GZIP)
- Automatic best-method selection
- Custom file format (ZDOC header)
- Temporary decompression with `--open`
- Windows CLI integration
- Progress bars
- Editable pip installation

## Installation

Clone the repository:

```bash
git clone https://github.com/Singh205/zipdoc.git
cd zipdoc
```

Install:

```bash
python -m pip install -e .
```

## Usage

Compress a file:

```bash
zipdoc file.txt
```

Open compressed file:

```bash
zipdoc file.txt --open
```

## Example Output

```
Compressed
Old: 50000
New: 8000
Saved: 42000
```

## Requirements

- Python 3.10+
- tqdm
- Ghostscript (for PDF compression)

## License

MIT License
