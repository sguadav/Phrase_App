import cv2
import pytesseract
import os
import instaloader
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program_Files\\Tesseract-OCR\\tesseract.exe'

# Get the Data from good instagram pages with quotes using:
# instaloader billionare_word
# instaloader thegoodquote
# On the terminal to download all the post from one profile

# only keep images files
data_directory = "C:\\Users\\sguad\\A_Projects\\Phrase_App\\Data_Processing\\data"

files_in_dir = os.listdir(data_directory)

for insta_account in files_in_dir:
    insta_account_path = os.path.join(data_directory, insta_account)
    current_account_path = os.listdir(insta_account_path)
    filtered_files = [file for file in current_account_path if file.endswith(".xz") or file.endswith(".mp4")]
    for file in filtered_files:
        path_to_file = os.path.join(insta_account_path, file)
        os.remove(path_to_file)


