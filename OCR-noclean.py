import pytesseract

from PIL import Image

import numpy as np

pytesseract.pytesseract.tesseract_cmd= r"C:\Users\mchee\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


img= Image.open(r"C:\Users\mchee\OneDrive - University of Waterloo\2022- Liaison Librarian Porter ISR\Scratch\PlainsAFrench\\Robarts.png")

text = pytesseract.image_to_string(img)

print(text)
