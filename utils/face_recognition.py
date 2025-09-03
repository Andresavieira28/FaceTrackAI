import face_recognition
import numpy as np

def detect_faces(frame):
    rgb = frame[:, :, ::-1]  # BGR para RGB
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)
    return locations, encodings

def compare_faces(known_encodings, new_encoding, tolerance=0.45):
    distances = face_recognition.face_distance(known_encodings, new_encoding)
    if len(distances) == 0:
        return None, None
    min_dist = np.min(distances)
    index = np.argmin(distances)
    return (index, min_dist) if min_dist < tolerance else (None, min_dist)
