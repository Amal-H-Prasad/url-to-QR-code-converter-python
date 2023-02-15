import qrcode

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add data to the QR code
data =input("enter your link :")
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")
