import pytesseract

from pytesseract import Output

from PIL import Image

import numpy as np

import cv2

pytesseract.pytesseract.tesseract_cmd= r"C:\Users\mchee\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


img= np.array(Image.open(r"C:\Users\mchee\OneDrive - University of Waterloo\2022- Liaison Librarian Porter ISR\Scratch\PlainsAFrench\\Robarts.png"))



norm_img=np.zeros((img.shape[0], img.shape[1]))

img=cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)

img=cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]

img=cv2.GaussianBlur(img, (1, 1), 0)



text = pytesseract.image_to_string(img)

print(text)
