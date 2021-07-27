import pytesseract
import cv2
import os
import PIL

from converting_images_for_ocr import converting_image_to_inverted

# Getting Tesseract working
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Getting the data folder and iterating through it
"""directory = r'C:\\Users\\sguad\\A_Projects\\Phrase_App\\Data_Processing\\data\\billionaire_word'
for filename in os.listdir(directory):
    if filename.endswith('jpg'):
        img_string = converting_image_to_inverted(os.path.join(directory, filename))
        print("---------")"""

# directory = 'C:\\Users\\sguad\\A_Projects\\Phrase_App\\Data_Processing\\' \
#             'data\\billionaire_word\\2020-05-21_15-45-42_UTC.jpg'
directory = 'C:\\Users\\sguad\\A_Projects\\Phrase_App\\Data_Processing\\' \
            'data\\billionaire_word\\2020-05-03_09-56-30_UTC.jpg'
img_string = converting_image_to_inverted(directory)

