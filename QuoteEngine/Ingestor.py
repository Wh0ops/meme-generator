from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """
    The Ingestor class encapsulates different ingestor strategies
    (CSV, DOCX, PDF, TXT) and selects the appropriate one based on
    the file extension.

    This class implements the `IngestorInterface` and acts as a facade
    to manage the ingestion of quotes from various file formats.
    """

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file using the appropriate ingestor and return a
        list of QuoteModel objects.

        Args:
            path (str): The file path.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from
            the file.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise ValueError(
            'No suitable ingestor found for file extension: '
            f'{path.split(".")[-1]}'
        )
