import pytesseract
from PIL import Image

img_file = "test-image.png"
img = Image.open(img_file)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

ocr_result = pytesseract.image_to_string(img)
print(ocr_result)