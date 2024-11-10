from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcodes(image: Image.Image):
    decoded_objects = decode(image)
    data = []
    for obj in decoded_objects:
        data.append(obj.data.decode('utf-8'))
    return data
