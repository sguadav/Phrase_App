import cv2.cv2
import pytesseract
from PIL import Image, ImageOps
import numpy as np

def converting_image_to_inverted(img_path):
    # img = Image.open(img_path).convert("L")
    # img = ImageOps.invert(img)
    # img.show()

    # trying gray scale
    img = cv2.imread(img_path)
    img_string = None
    cv2.imshow("test", img)
    cv2.waitKey(0)
    """ if img is not None:
        thresh_image = cv2.cvtColor(img, 127, 255, cv2.THRESH_BINARY)       # 127

        img_string = pytesseract.image_to_string(thresh_image, lang='eng')

        print(img_string)
        cv2.imshow("test", thresh_image)
        cv2.waitKey(0)
        return img_string"""

    """img = Image.open(img_path)
    img = ImageOps.invert(img)
    # img = ImageOps.grayscale(img)

    img = img.convert('1')  # convert image to black and white

    img_string = pytesseract.image_to_string(img, lang='eng')

    img.show()"""


    return img_string
