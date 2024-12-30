import streamlit as st
import qrcode
from io import BytesIO  # Used to create an in-memory buffer

# Title and description
st.title("QR Code Generator")
st.subheader("Enter the link you want to encode in the QR code")

# Text input for the link
user_input = st.text_input("Enter the link")

if user_input.strip():  # Check if the input is not empty
    # Generate the QR code using the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Convert the QR code image to bytes
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)  # Reset the pointer to the beginning of the buffer

    # Display the QR code
    st.image(buffer, caption="QR Code")

    # Provide a download button
    st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="QRCode.png",
        mime="image/png",
    )
