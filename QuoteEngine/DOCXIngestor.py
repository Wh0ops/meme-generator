import docx
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DOCXIngestor(IngestorInterface):
    """
    A concrete ingestor for DOCX files.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the DOCX file and return a list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f'Cannot ingest file with extension {path.split(".")[-1]}'
            )

        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text.strip():
                text = para.text.strip()

                if ' - ' in text:
                    body, author = text.split(' - ')
                    # Strip out any leading/trailing double quotes
                    body = body.strip('"').strip()
                    author = author.strip('"').strip()
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        return quotes
