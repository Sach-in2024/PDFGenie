import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import numpy as np
import cv2
from sklearn.cluster import KMeans

# Page config
st.set_page_config(
    page_title="Smart Image Recognition Chatbot",
    page_icon="🤖📷",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for softer light theme
st.markdown("""
    <style>
    .stApp {
        background-color: #f2f6ff;
        color: #1a1a1a;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 25px;
        font-size: 16px;
    }
    .stFileUploader>div {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    .stSidebar {
        background-color: #f7f9fc;
    }
    .stImage img {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar information
with st.sidebar:
    st.header("About")
    st.write("""
    This AI chatbot analyzes uploaded images and describes what's in them.
    It also detects dominant colors to give more details!
    """)
    st.write("Built with Streamlit, Transformers, OpenCV & Scikit-learn.")

# Load model once
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Function to detect dominant color
def detect_dominant_color(image, k=3):
    img = np.array(image)
    img = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_
    counts = np.bincount(kmeans.labels_)
    dominant = colors[counts.argmax()]
    return tuple(map(int, dominant))

# Function to map RGB to a basic color name
def rgb_to_name(rgb):
    r, g, b = rgb
    if r > 200 and g > 200 and b > 200:
        return "white"
    if r < 50 and g < 50 and b < 50:
        return "black"
    if r > 150 and g < 100 and b < 100:
        return "red"
    if r < 100 and g > 150 and b < 100:
        return "green"
    if r < 100 and g < 100 and b > 150:
        return "blue"
    if r > 150 and g > 150 and b < 100:
        return "yellow"
    if r > 150 and g < 100 and b > 150:
        return "purple"
    if r < 100 and g > 150 and b > 150:
        return "cyan"
    return "unknown"

# Main app
st.title("🤖 Smart Image Recognition Chatbot")
st.write("Upload an image and I’ll describe it and give extra details!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)

    with col2:
        with st.spinner("Analyzing image..."):
            # Caption generation
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs)
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Dominant color detection
            dom_color_rgb = detect_dominant_color(image)
            dom_color_name = rgb_to_name(dom_color_rgb)

        st.success("Analysis Complete!")
        st.markdown("### 📄 Description:")
        st.write(caption)

        st.markdown("### ✨ Extra Info:")
        st.write(f"**Dominant color detected:** {dom_color_name} (RGB: {dom_color_rgb})")

# Footer
st.markdown("---")
st.caption("Developed by Your Name | Powered by Streamlit, Transformers, OpenCV & Scikit-learn")
