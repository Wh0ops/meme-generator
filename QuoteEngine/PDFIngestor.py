import os
import subprocess
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """
    A concrete ingestor for PDF files.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the PDF file and return a list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f'Cannot ingest file with extension {path.split(".")[-1]}'
            )

        # Ensure tmp directory exists
        tmp_dir = './tmp'
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

        tmp = f'{tmp_dir}/{os.path.basename(path).replace(".pdf", ".txt")}'

        # Convert PDF to text using pdftotext
        try:
            subprocess.call(['pdftotext', path, tmp])
        except Exception as e:
            raise RuntimeError(
                f"Error occurred while converting PDF to text: {e}"
            )

        quotes = []
        with open(tmp, 'r', encoding='utf-8') as file:
            text = file.read()

            # Split based on quotes
            raw_quotes = text.split('"')

            for i in range(1, len(raw_quotes), 2):
                quote_body = raw_quotes[i].strip()
                if i + 1 < len(raw_quotes):
                    author_part = raw_quotes[i + 1]
                    author = (author_part.split('-')[-1].strip()
                              if '-' in author_part else "Unknown")
                    new_quote = QuoteModel(quote_body, author)
                    quotes.append(new_quote)

        # Clean up the temporary file
        os.remove(tmp)

        return quotes
