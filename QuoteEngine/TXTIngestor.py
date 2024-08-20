from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TXTIngestor(IngestorInterface):
    """
    A concrete ingestor for TXT files.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the TXT file and return a list of QuoteModel objects.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f'Cannot ingest file with extension {path.split(".")[-1]}'
            )

        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file.readlines():
                line = line.strip()
                if len(line) > 0:
                    body, author = line.split(' - ', 1)
                    new_quote = QuoteModel(body.strip(), author.strip())
                    quotes.append(new_quote)

        return quotes
