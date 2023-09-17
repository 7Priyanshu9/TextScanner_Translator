from pdf2image import convert_from_path

# Update the Poppler path with escaped backslashes
poppler_path = r'C:\Program Files\poppler-23.08.0\Library\bin'

# Provide the path to your PDF file
pdf_file_path = 'sample.pdf'

images = convert_from_path(pdf_file_path, 500, poppler_path=poppler_path)

for i, image in enumerate(images):
    image.save('page' + str(i) + '.jpg', 'JPEG')