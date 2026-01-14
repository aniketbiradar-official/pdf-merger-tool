import tkinter as tk
from tkinter import messagebox, filedialog
import logging
import os

from logger_config import setup_logger
from pdf_utils import get_pdf_files, merge_pdfs

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("500x250")

        self.selected_dir = ""

        # Title
        tk.Label(
            self.root,
            text="Select a directory to merge PDF files",
            font=("Arial", 12),
        ).pack(pady=10)

        # Browse Button
        tk.Button(
            self.root,
            text="Browse Directory",
            width=25,
            command=self.browse_directory
        ).pack(pady=5)

        # Directory Display
        self.dir_label = tk.Label(
            self.root,
            text="No directory selected",
            fg="blue",
            wraplength=450
        )
        self.dir_label.pack(pady=5)

        # Merge Button
        tk.Button(
            self.root,
            text="Merge PDFs",
            width=25,
            command=self.merge_action
        ).pack(pady=15)


    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_dir = directory
            self.dir_label.config(text=directory)
            logging.info(f"Directory selected: {directory}")


    def merge_action(self):
        if not self.selected_dir:
            messagebox.showerror("Error", "No directory selected")
            return

        pdf_files = get_pdf_files(self.selected_dir)

        if len(pdf_files) == 0:
            messagebox.showinfo("Info", "No PDF files found")
            return

        output_path = os.path.join(self.selected_dir, "merged_output.pdf")

        if merge_pdfs(pdf_files, output_path):
            messagebox.showinfo("Success", "PDFs merged successfully")
        else:
            messagebox.showerror("Error", "PDF merge failed")


if __name__ == "__main__":
    setup_logger()
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()