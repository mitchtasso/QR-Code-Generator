import qrcode

print("Hello! Welcome to the QR code generator.\n")
data = input("Please enter the link or data: ")
title = input("Please enter the title of the file: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4, 
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{title}_qrcode.png")
print(f"\nQR Code Generated: {title}_qrcode.png")