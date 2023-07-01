import cv2
import os
import threading
from image_capture import capture_images
from config import output_image_directory
from voice_recognition import voice_recognition

def run_voice_recognition():
    while True:
        voice_recognition()
        if not camera_window_open:
            break

os.makedirs(output_image_directory, exist_ok=True)

cap = cv2.VideoCapture(0)

image_count = 1

camera_window_open = True

voice_thread = threading.Thread(target=run_voice_recognition)
voice_thread.start()

while cap.isOpened() and camera_window_open:
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image_count = capture_images(image, output_image_directory, image_count)

    cv2.imshow('Body Tracking', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera_window_open = False
        break

    if cv2.getWindowProperty('Body Tracking', cv2.WND_PROP_VISIBLE) < 1:
        camera_window_open = False
        break

voice_thread.join()

cap.release()
cv2.destroyAllWindows()
