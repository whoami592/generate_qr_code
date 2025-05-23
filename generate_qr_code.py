# QR Code Generator
# Coded by Mr. Sabaz Ali Khan
# This script generates a QR code for a given URL and saves it as an image

import qrcode

# Define the data to encode in the QR code
data = "https://github.com/whoami592"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border thickness in boxes
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png' by Mr. Sabaz Ali Khan")