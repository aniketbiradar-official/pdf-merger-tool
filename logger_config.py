import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/pdf_merger.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        filemode="a"
    )

    logging.info("PDF Merger Tool Started")