import os
import PyPDF2
from pdf2image import convert_from_path
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas

def convert_pdf_to_image(pdf_path):
    return convert_from_path(pdf_path)[0]  # Assuming it's a single-page PDF

def extract_pdf_content(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        content = reader.getPage(0).extractText()
    return content

def overlay_text_on_image(image, text, position):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Choose a font and size that matches the original PDF
    draw.text(position, text, (0, 0, 0), font=font)  # Position needs to be where you want the text
    return image

def image_to_pdf(image, output_pdf_path):
    image.save(output_pdf_path, "PDF", resolution=100.0)

def process_resume(input_pdf, output_pdf):
    original_image = convert_pdf_to_image(input_pdf)
    content = extract_pdf_content(input_pdf)
    processed_content = content  # Add your processing logic here

    # You need to know the exact position where the text goes
    position = (50, 50)  # Example position, adjust as needed
    updated_image = overlay_text_on_image(original_image, processed_content, position)
    image_to_pdf(updated_image, output_pdf)

# File paths
input_pdf_path = r"C:\Users\raamc\OneDrive\Desktop\Resume\Raam_Charran_Resume.pdf"
output_pdf_path = os.path.join(os.path.dirname(input_pdf_path), "Processed_Raam_Charran_Resume.pdf")

# Process the resume
process_resume(input_pdf_path, output_pdf_path)
