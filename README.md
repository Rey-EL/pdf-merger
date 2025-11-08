# PDF Merger

A simple and efficient Graphical User Interface (GUI) application built with Python and Tkinter for merging multiple PDF files into a single document.

---

## Key Features

*   **Full GUI Application:** Built with `tkinter` for a simple, user-friendly interface.
*   **Recursive PDF Discovery:** Select a single folder, and the application will automatically find all `.pdf` files within that folder and all its subfolders.
*   **Ordered Merging:** Automatically sorts the found PDF files alphabetically by their full path to ensure a logical and predictable merge order.
*   **User-Controlled Saving:** Prompts the user with a native "Save As" dialog to let them choose the exact name and location for the final merged PDF.
*   **Robust Error Handling:** Safely handles corrupt or encrypted PDF files. If a file cannot be read, a warning is shown, and the script skips that file instead of crashing.
*   **Efficient Merging:** Uses the modern and actively maintained `pypdf` library for reliable performance.

---

## Installation & Setup

To run the PDF Merger application from the source script, you need Python 3.

1.  **Navigate to the project directory:**
    ```bash
    cd pdf-merger
    ```

2.  **Install dependencies:**
    It's highly recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install the required packages
    pip install -r requirements.txt
    ```

---

## Usage

1.  **Run the script from your terminal:**
    ```bash
    python3 merge_pdfs.py
    ```

2.  **Select a Folder:** Click the **"1. Select Folder with PDFs"** button and choose the folder containing the PDFs you want to merge.

3.  **Merge and Save:** Click the **"2. Merge and Save As..."** button. A "Save As" dialog will appear, allowing you to name your merged file and choose where to save it.

4.  **Done:** A success message will appear when the merge is complete.

---

## Creating a Standalone Executable (Optional)

You can bundle this application and its dependencies into a single standalone `.exe` file for Windows using **PyInstaller**. This allows it to be run on machines that do not have Python installed.

To build the executable:

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command from the project directory:**
    This command will create a `.spec` file and a `dist` folder containing the final `merge_pdfs.exe`.
    ```bash
    pyinstaller --onefile --windowed merge_pdfs.py
    ```

3.  The final `merge_pdfs.exe` will be located in the `dist` folder.
