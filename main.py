import qrcode
import streamlit as st
from PIL import Image as im

logo, title = st.columns([1,5])
with logo:
    st.image("logo.png", width=100)
with title:
    st.title("QR Code Generator")
st.set_page_config(page_title="QR Code Generator", page_icon="logo.png")

data = st.text_input("Input your URL or data to convert")
generate = st.button("Generate")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4, 
)

if generate:
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.jpg")
    st.image(image=im.Image.convert(img), width=200)
    with open("qrcode.jpg", "rb") as file:
        st.download_button(
            label="Download",
            data=file,
            file_name="qrcode.jpg",
            mime="image/png",
        )
