"""
Frontend Application for Image Caption Generator.

This Streamlit app allows users to upload an image and receive
a generated caption describing its contents using the LLaVA model.
"""

import os
import sys

import streamlit as st
import requests

PACKAGE_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from components import render_app_footer, run_with_status_updates

# Set the main title of the Streamlit app
st.title("Image Caption Generator (LLaVA)")

# Create a file uploader widget for images
# Users can select JPG, JPEG, or PNG files to upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display the uploaded image on the page
    # use_container_width=True makes the image responsive to page width
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Add empty space for visual separation
    st.write("")

    # Check if the user clicked the "Generate Caption" button
    if st.button("Generate Caption"):
        # Prepare the file for upload
        # Get the raw bytes of the uploaded file
        files = {"file": uploaded_file.getvalue()}

        # Send the image to the backend API for caption generation
        response = run_with_status_updates(
            lambda: requests.post(
                "http://localhost:8000/caption/",
                files=files
            ),
            start_message="Generating the image caption..."
        )

        # Check if the request was successful (HTTP 200)
        if response.status_code == 200:
            # Extract the caption from the JSON response
            caption = response.json().get("caption", "Error generating caption.")

            # Display the caption section header
            st.subheader("Generated Caption:")

            # Render the caption text on the page
            st.write(caption)
        else:
            # Display an error message if the backend request failed
            st.error("Error generating caption. Make sure the backend is running.")


render_app_footer()
