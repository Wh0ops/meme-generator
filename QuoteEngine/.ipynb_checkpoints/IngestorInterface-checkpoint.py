from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    An abstract base class for all ingestors.

    This class defines the interface for all file type ingestors,
    ensuring that they can check if they can ingest a given file type
    and parse the file into a list of QuoteModel objects.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the given file can be ingested.

        Args:
            path (str): The file path.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the file and return a list of QuoteModel objects.

        This method must be implemented by all subclasses.

        Args:
            path (str): The file path.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects parsed from file.
        """
        pass
