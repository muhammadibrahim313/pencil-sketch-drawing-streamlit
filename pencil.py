import streamlit as st
import numpy as np
from PIL import Image
import cv2

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def pencilsketch(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21,21),sigmaX=0, sigmaY=0)
    final_img = dodgeV2(img_gray, img_smoothing)
    return(final_img)

# Customizing Streamlit App
st.set_page_config(
    page_title="PencilSketcher",
    page_icon=":pencil2:",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main-container {
            padding: 2rem;
        }
        .social-media {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }
        .social-media a {
            margin: 0 10px;
            text-decoration: none;
        }
        .social-media img {
            width: 50px;
            height: 50px;
            filter: grayscale(1); /* Convert images to grayscale for professional look */
        }
        .social-media img:hover {
            filter: grayscale(0); /* Remove grayscale filter on hover */
        }
        .title {
            text-align: center;
            color: #333;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .description {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<h1 class='title'>PencilSketcher</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>This web app converts your photos into realistic pencil sketches.</p>", unsafe_allow_html=True)

# Social media links
st.sidebar.title("About Me 👋 🌐:")  
st.sidebar.markdown("I am a passionate 👩‍💻data analyst and I love to build web applications✨ and coding and I am always looking for new and exciting projects to work on✨.")
st.sidebar.title("Connect with Me🌐💡🤝:")
st.sidebar.markdown("[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/)")
st.sidebar.markdown("[![GitHub](https://img.icons8.com/ios-filled/50/000000/github.png)](https://github.com/muhammadibrahim313)")
st.sidebar.markdown("[![Kaggle](https://img.icons8.com/color/48/000000/kaggle.png)](https://www.kaggle.com/muhammadibrahimqasmi)")

# File uploader
file_image = st.sidebar.file_uploader("Upload Image", type=['jpeg','jpg','png'])

# Functionality to convert images into pencil sketches
if file_image is not None:
    input_img = Image.open(file_image)
    final_sketch = pencilsketch(np.array(input_img))
    
    # Display Input and Output images
    st.subheader("Input Photo")
    st.image(input_img, use_column_width=True, caption="Original Image")
    
    st.subheader("Output Pencil Sketch")
    st.image(final_sketch, use_column_width=True, caption="Pencil Sketch")
else:
    st.write("Please upload an image to start processing.")
