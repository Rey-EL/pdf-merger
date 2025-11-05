# PDF Merger

## Description

This is a simple and efficient Graphical User Interface (GUI) application built in Python for merging multiple PDF files into a single document.

## Features

*   **Full GUI Application:** Built with `tkinter`, providing a user-friendly interface with buttons for all actions.
*   **Select Folder:** The user can select a folder, and the script will automatically find all `.pdf` files within that folder and all its subfolders.
*   **"Save As" Dialog:** Prompts the user with a "Save As" dialog box to let them choose the name and location for their final merged PDF.
*   **Reliable Merging:** Uses the `pypdf` library to append all found PDFs.
*   **Ordered Merging:** Automatically sorts the found PDF files alphabetically to ensure a logical order before merging.

## Error Handling

Safely handles corrupt or encrypted PDF files. If a file cannot be merged, it will show a warning and skip that file instead of crashing.

## Deployment / Executable

A `merge_pdfs.spec` file is included in this repository. This file is a "recipe" for PyInstaller, which compiles this Python script into a standalone `merge_pdfs.exe` for Windows (note the `console=False` flag, which makes it a true windowed app). This allows the tool to be run on any Windows machine, even one that does not have Python installed. The final `.exe` is generated in the `dist` folder.

## How to Use (Script)

1.  Run the script from your terminal: `python3 merge_pdfs.py`
2.  Click the "1. Select Folder with PDFs" button and choose your folder.
3.  Click the "2. Merge and Save As..." button to choose where to save your new file.
4.  A success message will appear when the merge is complete.