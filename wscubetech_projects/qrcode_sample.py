
##  don't give file name as : qrcode.py

import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,border=4)

# Add data to the QR Code
qr.add_data('https://www.example.com')
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save('qrcode_example.png')

# Optionally, open and display the image
img.show()
