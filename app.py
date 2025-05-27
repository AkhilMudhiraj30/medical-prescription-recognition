from PIL import Image
import pytesseract

# Load a sample image of a prescription
img = Image.open('prescription_sample.jpg')

# Apply OCR to extract text
text = pytesseract.image_to_string(img)

print("Extracted Text:\n", text)
