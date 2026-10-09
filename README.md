# pdf-merger

I kept needing to combine scattered PDFs into one file, so I built this small GUI for it.

![CI](https://github.com/Rey-EL/pdf-merger/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- Finds every PDF in a folder, including subfolders
- Merges them in alphabetical path order
- Skips corrupt or encrypted files with a warning instead of crashing
- Lets you pick the output name and location with a Save As dialog

## Install

```bash
git clone https://github.com/Rey-EL/pdf-merger.git
cd pdf-merger
pip install -r requirements.txt
```

## Usage

```bash
python3 pdf_merger.py
```

1. Click "1. Select Folder with PDFs" and pick the folder.
2. Click "2. Merge and Save As..." and choose where the merged file goes.

## How it works

The merge logic (`merge_pdfs_in_folder`) walks the folder, sorts the PDFs, and appends them one by one with pypdf. A file that fails to append is reported and skipped; the rest still merge. Tests live in `tests/` and run on Python 3.10–3.12 in CI.

## Project structure

```
pdf-merger/
├── pdf_merger.py             # the tool (merge logic + tkinter GUI)
├── requirements.txt
├── tests/                    # pytest suite (merge logic only)
└── .github/workflows/ci.yml  # CI workflow
```

## License

MIT — see [LICENSE.md](LICENSE.md).
