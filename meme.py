import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine
import os


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an image path and a quote """
    img = path if path else random.choice(
        [os.path.join("./_data/photos/dog", file)
         for file in os.listdir("./_data/photos/dog")]
    )

    quote = None
    if body is None or author is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv"
        ]
        quote_file = random.choice(quote_files)
        quotes = Ingestor.parse(quote_file)
        quote = random.choice(quotes)
    else:
        quote = QuoteModel(body, author)

    meme = MemeEngine('./output')
    output_path = meme.make_meme(img, quote.body, quote.author)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a meme with a quote.")
    parser.add_argument('--path', type=str, help="Path to the image file.")
    parser.add_argument('--body', type=str, help="Quote body text.")
    parser.add_argument('--author', type=str, help="Quote author.")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
