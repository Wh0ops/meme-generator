class QuoteModel:
    """
    A simple class to encapsulate a quote's body and author.

    Attributes:
        body (str): The body of the quote.
        author (str): The author of the quote.
    """

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel instance.

        Args:
            body (str): The body of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return a string representation of the quote."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Return a string representation for debugging."""
        return f'QuoteModel(body="{self.body}", author="{self.author}")'
