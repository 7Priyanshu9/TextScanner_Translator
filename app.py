import pytesseract
from PIL import Image
from googletrans import Translator

myconfig = r"--psm 6 --oem 3"

# Open the image and perform text extraction
image_path = "tiger.jpg"
img = Image.open(image_path)
text = pytesseract.image_to_string(img, config=myconfig)

# Print the extracted text
print("Extracted Text:")
print(text)

# Language selection menu
print("\nSelect a language for translation:")
print("1. Bengali (bn)")
print("2. Hindi (hi)")
print("3. Telugu (te)")
print("4. Tamil (ta)")
print("5. Urdu (ur)")
print("6. Gujrati (gu)")
print("7. Kannada (kn)")
print("8. Malayalam (ml)")
print("9. Marathi (mr)")
print("10. Nepali (ne)")
print("11. Odia (or)")
print("12. Punjabi (pa)")
print("13. Sindhi (sd)")

choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

# Translate the extracted text based on the user's choice
translator = Translator()

if choice == "1":
    op = translator.translate(text, dest="bn")
elif choice == "2":
    op = translator.translate(text, dest="hi")
elif choice == "3":
    op = translator.translate(text, dest="te")
elif choice == "4":
    op = translator.translate(text, dest="ta")
elif choice == "5":
    op = translator.translate(text, dest="ur")
elif choice == "6":
    op = translator.translate(text, dest="gu")
elif choice == "7":
    op = translator.translate(text, dest="kn")
elif choice == "8":
    op = translator.translate(text, dest="ml")
elif choice == "9":
    op = translator.translate(text, dest="mr")
elif choice == "10":
    op = translator.translate(text, dest="ne")
elif choice == "11":
    op = translator.translate(text, dest="or")
elif choice == "12":
    op = translator.translate(text, dest="pa")
elif choice == "13":
    op = translator.translate(text, dest="sd")
else:
    print("Invalid choice. Using default target language (Bengali).")
    op = translator.translate(text, dest="bn")

# Print the translated text
print("\nTranslated Text:")
print(op.text)
