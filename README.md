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

Installing Ghostscript (Windows)

1. Download from the official site:
   https://www.ghostscript.com/releases/gsdnld.html

2. Install the Windows 64-bit version.

3. After installation, verify:

```bash
gswin64c --version
```

If it prints a version number, Ghostscript is installed correctly.

---

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
