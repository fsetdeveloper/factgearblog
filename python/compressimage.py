# Python utility to compress images in a directory
# to optimize the image for web page and blog

import os
import sys
import argparse
from PIL import Image

def compress_image(input_dir, quality=85, max_width=800, max_height=800):
    for filename in os.listdir(input_dir):
        print(filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) and filename == 'catalog.jpg':
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            
            # Resize the image
            img.thumbnail((max_width, max_height), Image.LANCZOS)
            
            # Save the image with the specified quality
            img.save(img_path, quality=quality, optimize=True)

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Adjust the path to the images folder
images_dir = os.path.join(current_dir, '../static/images')

# Call the function with the adjusted path
compress_image(images_dir, quality=85)
