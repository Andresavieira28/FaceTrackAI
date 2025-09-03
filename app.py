import streamlit as st
import cv2
import face_recognition
import numpy as np
import os

st.set_page_config(layout="centered", page_title="FaceTrackAI")
st.title("🎯 FaceTrackAI - Reconhecimento Facial")

run = st.checkbox('Ativar câmera')
FRAME_WINDOW = st.image([])

# Carregar rostos conhecidos (se houver)
known_face_encodings = []
known_face_names = []

for file in os.listdir("known_faces"):
    if file.endswith(".jpg") or file.endswith(".png"):
        img = face_recognition.load_image_file(f"known_faces/{file}")
        enc = face_recognition.face_encodings(img)
        if enc:
            known_face_encodings.append(enc[0])
            known_face_names.append(file.split(".")[0])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        cv2.rectangle(rgb_frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(rgb_frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    FRAME_WINDOW.image(rgb_frame)

else:
    st.write('Câmera desligada.')
