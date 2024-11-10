import io
import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
from utils.ocr import extract_text_from_image
from utils.barcode_reader import decode_barcodes
from services.tokenizer import tokenizar_texto


def procesar_pdf_bytes(pdf_bytes):
    pares_paginas = []
    reader = PdfReader(io.BytesIO(pdf_bytes))


    num_pages = len(reader.pages)
    for i in range(0, num_pages, 2):
        texto_pag_1 = ""
        texto_pag_2 = ""


        page_1 = reader.pages[i]
        text_1 = page_1.extract_text()
        if text_1:
            texto_pag_1 += text_1


        if i + 1 < num_pages:
            page_2 = reader.pages[i + 1]
            text_2 = page_2.extract_text()
            if text_2:
                texto_pag_2 += text_2


        poppler_path = r'C:\Users\devel\Desktop\pdfToToken\Release-24.07.0-0\poppler-24.07.0\Library\bin'
        images = convert_from_bytes(pdf_bytes, first_page=i + 1, last_page=i + 2, poppler_path=poppler_path)


        text_image_1 = extract_text_from_image(images[0])
        texto_pag_1 += f"\n{text_image_1}"
        decoded_data_1 = decode_barcodes(images[0])
        texto_pag_1 += f"\n{' '.join(decoded_data_1)}"


        if i + 1 < len(images):
            text_image_2 = extract_text_from_image(images[1])
            texto_pag_2 += f"\n{text_image_2}"
            decoded_data_2 = decode_barcodes(images[1])
            texto_pag_2 += f"\n{' '.join(decoded_data_2)}"


        pares_paginas.append((texto_pag_1, texto_pag_2))

    return pares_paginas
