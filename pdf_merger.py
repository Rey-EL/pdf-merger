# Copyright (c) 2025 Elvis Reyes
#
# This software is licensed under the MIT License.
# See the LICENSE.md file in the project root for full license terms.

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter

def merge_pdfs_in_folder(folder_path, full_output_path):
    """
    Merges PDFs and saves them to the user-specified full path.
    Returns a status message for the GUI.
    """
    pdf_writer = PdfWriter()
    pdf_files = []

    # Walk through the directory to find all PDF files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_path = os.path.join(root, file)
                pdf_files.append(full_path)

    if not pdf_files:
        return "No PDF files found in the selected folder."

    # Sort the files alphabetically for a logical order
    pdf_files.sort()

    # Append each PDF
    for path in pdf_files:
        try:
            pdf_writer.append(path)
        except Exception as e:
            messagebox.showwarning("File Error", f"Could not merge '{os.path.basename(path)}'. It may be corrupt or encrypted.\n\nReason: {e}")
            
    # Write the merged PDF to the path chosen by the user
    try:
        with open(full_output_path, "wb") as out_file:
            pdf_writer.write(out_file)
        return f"Success! ✅\n\n{len(pdf_files)} PDFs merged into:\n{full_output_path}"
    except Exception as e:
        return f"Error saving file: {e}"
    finally:
        pdf_writer.close()


# --- GUI Application Code ---
class PdfMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("450x150") # Adjusted window size

        # Folder selection
        self.folder_label = tk.Label(root, text="No folder selected.", wraplength=400)
        self.folder_label.pack(pady=10)
        
        self.select_button = tk.Button(root, text="1. Select Folder with PDFs", command=self.select_folder)
        self.select_button.pack(pady=5)

        # Merge and Save button
        self.merge_button = tk.Button(root, text="2. Merge and Save As...", command=self.run_merge)
        self.merge_button.pack(pady=20)
        
        self.selected_folder = ""

    def select_folder(self):
        # Open a dialog to select a folder
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=f"Selected: {folder}")

    def run_merge(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return
        
        # --- THIS IS THE NEW PART ---
        # Open a "Save As" dialog
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            title="Save Merged PDF As..."
        )
        # If the user cancels the save dialog, stop the process
        if not output_path:
            return
        # --- END OF NEW PART ---

        # Run the merge function and show the result in a message box
        status = merge_pdfs_in_folder(self.selected_folder, output_path)
        messagebox.showinfo("Result", status)

if __name__ == "__main__":
    root = tk.Tk()
    app = PdfMergerApp(root)
    root.mainloop()
