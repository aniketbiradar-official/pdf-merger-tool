import os
import logging
from PyPDF2 import PdfMerger

def get_pdf_files(directory):
    pdfs = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.lower().endswith(".pdf")
    ]
    logging.info(f"PDF count: {len(pdfs)}")
    return pdfs

def merge_pdfs(pdf_files, output_path):
    try:
        merger = PdfMerger()

        for pdf in pdf_files:
            merger.append(pdf)

        merger.write(output_path)
        merger.close()

        logging.info(f"Merged PDF created at {output_path}")
        return True

    except Exception as e:
        logging.error("PDF merge failed")
        logging.exception(e)
        return False