import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os
import tensorflow as tf
from keras.src.legacy.saving import legacy_h5_format
from keras.models import load_model

# Set page configuration
st.set_page_config(
    page_title="Age & Gender Detector",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2563EB;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .result-text {
        font-size: 1.5rem;
        font-weight: 500;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .image-container {
        margin-bottom: 2rem;
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: rgba(237, 242, 247, 0.5);
    }
    
    .app-footer {
        text-align: center;
        margin-top: 2rem;
        opacity: 0.7;
    }
    
    .stButton>button {
        background-color: #2563EB;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        border: none;
    }
    
    .stButton>button:hover {
        background-color: #1E40AF;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Function to load the model (with caching for performance)
@st.cache_resource
def load_age_gender_model():
    try:
        model_path = r"C:\Learning\age_gender_code\Age_Sex_Detection.h5"
        model = legacy_h5_format.load_model_from_hdf5(
            model_path, custom_objects={"mae": "mae"}
        )
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None


# Function to preprocess the image
def preprocess_image(uploaded_image):
    # Convert to RGB if needed
    if uploaded_image.mode != "RGB":
        uploaded_image = uploaded_image.convert("RGB")

    # Resize to 48x48
    image = uploaded_image.resize((48, 48))

    # Convert to numpy array and normalize
    image_array = np.array(image) / 255.0

    # Expand dimensions for model input
    return np.expand_dims(image_array, axis=0)


# Function to make prediction
def predict_age_gender(model, image_array):
    try:
        predictions = model.predict(image_array)

        # Get age prediction (assuming age is second output)
        predicted_age = int(np.round(predictions[1][0]))

        # Get gender prediction (assuming gender is first output)
        gender_prob = predictions[0][0]
        predicted_gender = "Female" if gender_prob > 0.5 else "Male"
        gender_confidence = (
            gender_prob if predicted_gender == "Female" else 1 - gender_prob
        )

        return predicted_age, predicted_gender, float(gender_confidence)
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None, None, None


# Helper function to convert hex color to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


# Main function
def main():
    # Header
    st.markdown(
        '<div class="main-header">Age and Gender Detector</div>', unsafe_allow_html=True
    )

    # Load model
    with st.spinner("Loading model... This may take a moment."):
        model = load_age_gender_model()

    if model is None:
        st.warning("Please make sure the model file exists at the specified path.")
        return

    # File uploader - Allow multiple files
    st.markdown('<div class="sub-header">Upload Images</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "Choose one or more images...",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    # Process button
    if uploaded_files and st.button("Detect Age & Gender"):
        with st.spinner("Analyzing images..."):
            # Process each image
            for i, uploaded_file in enumerate(uploaded_files):
                # Create a container for each image and its results
                with st.container():
                    st.markdown(
                        f'<div class="image-container">', unsafe_allow_html=True
                    )

                    # Display image number
                    st.markdown(f"<h3>Image {i+1}</h3>", unsafe_allow_html=True)

                    # Create two columns for image and results
                    col1, col2 = st.columns([1, 1])

                    # Display uploaded image
                    image = Image.open(uploaded_file)
                    col1.image(
                        image,
                        caption=f"Image {i+1}: {uploaded_file.name}",
                        use_column_width=True,
                    )

                    # Process image
                    processed_image = preprocess_image(image)
                    age, gender, confidence = predict_age_gender(model, processed_image)

                    if age is not None and gender is not None:
                        # Display results with nice formatting
                        col2.markdown(
                            '<div class="sub-header">Results:</div>',
                            unsafe_allow_html=True,
                        )

                        # Age result
                        col2.markdown(
                            f'<div class="result-text" style="background-color: rgba(37, 99, 235, 0.1);">Age: {age}</div>',
                            unsafe_allow_html=True,
                        )

                        # Gender result with confidence
                        gender_color = "#9F7AEA" if gender == "Female" else "#4F46E5"
                        col2.markdown(
                            f'<div class="result-text" style="background-color: rgba({", ".join(map(str, hex_to_rgb(gender_color)))}, 0.1);">'
                            f"Gender: {gender}<br>"
                            f"<small>Confidence: {confidence:.2%}</small>"
                            f"</div>",
                            unsafe_allow_html=True,
                        )
                    else:
                        col2.error("Failed to process this image")

                    st.markdown("</div>", unsafe_allow_html=True)

                    # Add a separator between images
                    if i < len(uploaded_files) - 1:
                        st.markdown("<hr>", unsafe_allow_html=True)

    # Show message if no files uploaded
    elif st.button("Detect Age & Gender"):
        st.info("Please upload one or more images first.")

    # Footer
    st.markdown(
        '<div class="app-footer">Powered by NULLCLASS🧑‍💻</div>', unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
