import qrcode
import os

# Replace this URL with your Streamlit app's URL
streamlit_app_url = "https://emosync-2nn4hj4fpnhfz3uesjvhd6.streamlit.app/"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(streamlit_app_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

desktop_path = os.path.expanduser("~/Desktop")
save_path = os.path.join(desktop_path, "testing", "streamlit_app_qr.png")
img.save(save_path)

# Save the image to a file
img.save("Desktop/testing/streamlit_app_qr.png")
