import random
import os
import requests
from flask import Flask, render_template, request, redirect
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    # Load quotes from various file types
    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv"
    ]

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    # Load images from directory
    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, img) for img in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """

    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user-defined meme """

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    # Download the image
    try:
        response = requests.get(image_url)
        tmp = f'./static/{random.randint(0, 100000000)}.jpg'
        with open(tmp, 'wb') as f:
            f.write(response.content)

        path = meme.make_meme(tmp, body, author)

        # Remove the temporary image file
        os.remove(tmp)

        return render_template('meme.html', path=path)

    except Exception as e:
        print(f"An error occurred: {e}")
        return redirect('/create')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
