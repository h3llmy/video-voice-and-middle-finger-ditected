import cv2
import os
import time

def save_image(image_count, image, output_directory):
    image_filename = f"image_{int(time.time())}_{image_count}.jpg"
    image_path = os.path.join(output_directory, image_filename)
    cv2.imwrite(image_path, image)
    print(f"Image saved: {image_path}")
    image_count += 1
    return image_count