from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine:
    def __init__(self, output_dir: str):
        """
        Initialize the MemeEngine with an output directory.
        Args:
            output_dir (str): Directory where the manipulated images
                              will be saved.
        """
        self.output_dir = output_dir
        self.count = 1  # Initialize a counter for unique filenames
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path: str, text: str, author: str,
                  width: int = 500) -> str:
        """
        Create a meme with the provided image and text.
        Args:
            img_path (str): Path to the input image.
            text (str): The quote body to add to the image.
            author (str): The quote author to add to the image.
            width (int): The desired width of the image.
                         Default is 500px.
        Returns:
            str: Path to the saved manipulated image.
        """
        try:
            # Load the image
            img = Image.open(img_path)

            # Resize the image using LANCZOS for high-quality downsampling
            real_width, real_height = img.size
            height = int(real_height * width / real_width)
            img.thumbnail((width, height))

            # Prepare the text to add to the image
            draw = ImageDraw.Draw(img)

            # Load fonts for the quote and author
            quote_font_path = (
                'C:/Users/bronz/Downloads/meme-generator-By-Hamad-Fouzan/'
                '_data/fonts/Fashion Fetish Bold.ttf'
            )
            author_font_path = (
                'C:/Users/bronz/Downloads/meme-generator-By-Hamad-Fouzan/'
                '_data/fonts/Fashion Fetish Light Italic.ttf'
            )
            quote_font = ImageFont.truetype(quote_font_path, size=22)
            author_font = ImageFont.truetype(author_font_path, size=18)

            # Randomly select a vertical position for the text
            text_position = random.choice(range(30, height - 50))
            fill = (0, 0, 0)  # Black text color
            stroke_fill = (255, 255, 255)  # White stroke color

            # Draw the quote and author on the image with stroke
            draw.text(
                (30, text_position), text, font=quote_font, fill=fill,
                stroke_width=1, stroke_fill=stroke_fill
            )
            draw.text(
                (40, text_position + 25), f"- {author}", font=author_font,
                fill=fill, stroke_width=1, stroke_fill=stroke_fill
            )

            # Save the image with a unique filename
            outfile = os.path.join(self.output_dir, f"temp-{self.count}.jpg")
            img.save(outfile, "JPEG")
            self.count += 1  # Increment the counter for the next meme

            return outfile

        except Exception as e:
            print(f'An error occurred: {e}')
            return None
