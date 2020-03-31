import cv2
import pytesseract
from pytesseract import Output

# Load an color image in grayscale
pathImg = r'C:\Users\User\Desktop\opencv-text-recognition\opencv-text-recognition\images\example_01.jpg'
img = cv2.imread("example_01.jpg",0)
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())   
