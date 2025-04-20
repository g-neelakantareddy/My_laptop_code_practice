import cv2
import pytesseract
from pytesseract import Output

# Load and preprocess image
image_file = cv2.imread('sing_in.png')
gray = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite('processed.png', thresh)

# OCR to extract text
data = pytesseract.image_to_string(image_file)

# Split into lines and remove empty lines
split = data.lower().splitlines()
clean = [line.strip() for line in split if line.strip() != ""]

# Join cleaned lines back into one string
joined = "\n".join(clean)

# Debug print
print(joined)

# Check if 'sign in' is present
if 'sign in' in joined:
    print("True")
else:
    print("False")
