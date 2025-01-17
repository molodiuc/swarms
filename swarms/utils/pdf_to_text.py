import sys
import os

try:
    import PyPDF2
except ImportError:
    print(
        "PyPDF2 not installed. Please install it using: pip install"
        " PyPDF2"
    )
    sys.exit(1)


def pdf_to_text(pdf_path):
    """
    Converts a PDF file to a string of text.

    Args:
        pdf_path (str): The path to the PDF file to be converted.

    Returns:
        str: The text extracted from the PDF.

    Raises:
        FileNotFoundError: If the PDF file is not found at the specified path.
        Exception: If there is an error in reading the PDF file.
    """
    try:
        # Open the PDF file
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""

            # Iterate through each page and extract text
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"

            return text
    except FileNotFoundError:
        raise FileNotFoundError(
            f"The file at {pdf_path} was not found."
        )
    except Exception as e:
        raise Exception(
            f"An error occurred while reading the PDF file: {e}"
        )


# Example usage
# text = pdf_to_text("test.pdf")
# print(text)
