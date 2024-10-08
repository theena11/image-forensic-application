# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WxTpG003Xtgygliy0gx-0FNbKwMuR3gH
"""

pip install gradio

pip install gradio imagehash pillow

import gradio as gr
from PIL import Image
import imagehash

def calculate_image_hash(image):
    """Calculate the hash of an image."""
    return imagehash.average_hash(image)

def compare_images(image1, image2):
    """Compare two images based on their hashes."""
    hash1 = calculate_image_hash(image1)
    hash2 = calculate_image_hash(image2)
    return hash1 == hash2

def gradio_interface(image1, image2):
    """Interface function for Gradio."""
    if compare_images(image1, image2):
        return "The images are identical."
    else:
        return "The images are different."

# Define the Gradio interface
interface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Image(type="pil", label="Upload First Image"),
        gr.Image(type="pil", label="Upload Second Image")
    ],
    outputs="text",
    title="Image Forensics Application",
    description="Upload two images to check if they are identical based on their hash values. This can help detect image tampering."
)

if __name__ == "__main__":
    interface.launch()