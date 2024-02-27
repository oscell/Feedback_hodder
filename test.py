from google.cloud import vision

# Create a client
client = vision.ImageAnnotatorClient()

# Load an image file
with open("Images/form_1/Q1/Q1.jpg", "rb") as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Request document text detection
response = client.document_text_detection(image=image)

print(response.full_text_annotation.text)   
