# Meme Generator Project

## Overview
The Meme Generator project is a Python application designed to dynamically create memes by overlaying quotes onto images. The project demonstrates the use of object-oriented programming principles, image manipulation with the Pillow library, and the processing of various file formats to extract and use quotes.

## Features
- **Image Processing**: Load, resize, and manipulate images using the Pillow library.
- **Quote Ingestion**: Extract quotes from multiple file formats (CSV, DOCX, PDF, TXT).
- **Dynamic Meme Creation**: Overlay quotes onto images with customizable fonts and positions.
- **Command-Line Interface**: Generate memes using a command-line tool with optional arguments for quote body, author, and image path.
- **Web Service**: A Flask-based web service that generates memes using user input or random selection.

## Setup and Installation

### Prerequisites
- Python 3.x
- Pillow library
- Flask library
- Required Fonts: Ensure that the fonts `Fashion Fetish Bold.ttf` and `Fashion Fetish Light Italic.ttf` are available in the `_data/fonts` directory.

## Sub-modules Overview

1. **`QuoteEngine`**  
   The `QuoteEngine` module is responsible for ingesting quotes from various file formats. It includes:
   - **`QuoteModel`**: Encapsulates the quote body and author.
   - **`IngestorInterface`**: Abstract base class defining methods for quote ingestion.
   - **`CSVIngestor`, `DOCXIngestor`, `PDFIngestor`, and `TXTIngestor`**: Implementations for ingesting quotes from CSV, DOCX, PDF, and TXT files.
   - **`Ingestor`**: Encapsulates the individual ingestors and selects the appropriate one based on file type.

2. **`MemeEngine`**  
   The `MemeEngine` module is responsible for creating memes by overlaying quotes onto images. It handles:
   - **Loading and Resizing**: Resizes the image to fit within a specified width.
   - **Text Overlay**: Adds the quote and author to the image using specified fonts and positions.
   - **File Saving**: Saves the generated meme with a unique filename.

## Command-Line Tool

### Usage
The `meme.py` script allows users to generate memes via the command line. It accepts three optional arguments:
- `--body`: A string representing the quote body.
- `--author`: A string representing the quote author.
- `--path`: A string representing the image path.

### Example Command
```sh
python3 meme.py --body "This is a test quote" --author "Author Name" --path "./_data/photos/dog/xander_1.jpg" 
```
If any argument is not provided, the script will randomly select an image and/or quote.

## Web Service

### Running the Flask App
The 'app.py' script starts a Flask web service that allows users to generate memes through a web interface.

### Routes
- '/': Generates a random meme using a randomly selected image and quote.
- '/create': Provides a form for users to input an image URL, quote body, and author. Generates a meme based on the input.

### Starting the Server
```sh
python3 app.py
```
Navigate to 'http://localhost:3000' in your browser to use the web service.

### Dependencies
- Pillow: Used for image processing.
- Flask: Provides the web service.
- requests: Used for fetching images from URLs.
- Python-docx, PyPDF2: Used for extracting text from DOCX and PDF files, respectively.

## Installation
1. Clone the repository:
   
```sh
git clone <repository-url>
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt 
```

### Additional Information
- All code adheres to PEP-8 standards and includes proper error handling.
- Ensure that the required fonts are correctly placed in the '_data/fonts' directory for the `MemeEngine` to function correctly.
