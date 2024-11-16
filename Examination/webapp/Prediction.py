import os
import numpy as np
from keras.preprocessing import image
import cv2
import sys
import pickle
from sklearn import metrics
from keras.models import Sequential, load_model
from .inference import detect_faces
from .inference import draw_text
from .inference import draw_bounding_box
from .inference import apply_offsets
from .inference import load_detection_model
from .preprocessor import preprocess_input


def predict_emo():
    detection_model_path = 'C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\models\\haarcascade_frontalface_default.xml'
    emotion_model_path = 'C:\\Users\\SIDDHI\\Downloads\\Django\\Django\\Examination\\models\\cnn_model.hdf5'
    emotion_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}


    frame_window = 10
    emotion_offsets = (20, 40)
    emotion_text = ""

    # loading models
    face_detection = load_detection_model(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)

    # getting input model shapes for inference
    emotion_target_size = emotion_classifier.input_shape[1:3]
    DIRECTORY = "testing"
    CATEGORIES = [ "Angry", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

    predicted = []
    actual = []
    res='Neutral'
    if True:
        bgr_image = cv2.imread('cameraimg1.jpg')
        print(bgr_image)
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces = detect_faces(face_detection, gray_image)
        for face_coordinates in faces:
            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue
            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            
            draw_bounding_box(face_coordinates, bgr_image, [22,22,22])
            draw_text(face_coordinates, bgr_image, emotion_text,[22,22,22], 0, -45, 1, 1)
            bgr_image = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite("out.jpg",bgr_image)



        predicted.append(emotion_text)
        print(predicted)
        try:res=predicted[0]
        except:pass
        return predicted[0]





if __name__ == '__main__':
    predict_emo()
