import cv2
import mediapipe as mp
from save_image import save_image

mp_hands = mp.solutions.hands

def capture_images(image, output_directory, image_count):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(
        max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as hands:
        results_hands = hands.process(image_rgb)

        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                if (
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
                    hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y and
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                ):
                    image_count = save_image(image_count, image, output_directory)
    return image_count
