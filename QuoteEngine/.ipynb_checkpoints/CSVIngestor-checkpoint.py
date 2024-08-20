import csv
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """
    A concrete ingestor for CSV files.

    This class implements the `IngestorInterface` and is responsible
    for parsing quotes from CSV files.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the CSV file and return a list of QuoteModel objects.

        Args:
            path (str): The file path to the CSV file.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed
            from the CSV file.
        """
        if not cls.can_ingest(path):
            raise ValueError(
                f'Cannot ingest file with extension {path.split(".")[-1]}'
            )

        quotes = []
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_quote = QuoteModel(row['body'], row['author'])
                quotes.append(new_quote)

        return quotes
