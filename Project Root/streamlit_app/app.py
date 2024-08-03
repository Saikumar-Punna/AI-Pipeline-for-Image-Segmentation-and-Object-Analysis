import streamlit as st
from PIL import Image
import os
import json

def load_image(image_file):
    img = Image.open(image_file)
    return img

st.title("AI Pipeline for Image Segmentation and Object Analysis")

image_file = st.file_uploader("Upload Image", type=["jpg", "png"])

if image_file is not None:
    st.image(load_image(image_file), caption='Uploaded Image', use_column_width=True)
    with open(os.path.join("data/input_images", image_file.name), "wb") as f:
        f.write(image_file.getbuffer())
    st.success("File Uploaded Successfully")

    if st.button("Run Pipeline"):
        # Assume we have a function `run_pipeline` to execute the entire pipeline
        run_pipeline(os.path.join("data/input_images", image_file.name))

        # Display segmented objects
        segmented_dir = "data/segmented_objects/"
        for img_name in os.listdir(segmented_dir):
            st.image(load_image(os.path.join(segmented_dir, img_name)), caption=img_name, use_column_width=True)
        
        # Display the final output image
        st.image(load_image("data/output/annotated_image.jpg"), caption='Final Output Image', use_column_width=True)

        # Display the summary table
        st.dataframe(pd.read_csv("data/output/summary_table.csv"))
