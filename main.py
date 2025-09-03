from utils import video, face_recognition as fr, storage
import cv2

face_db = storage.load_faces()

def process_frame(frame):
    locations, encodings = fr.detect_faces(frame)

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        idx, dist = fr.compare_faces(face_db["encodings"], encoding)

        if idx is not None:
            name = face_db["names"][idx]
        else:
            name = "Desconhecido"
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            print("Novo rosto detectado!")
            nome = input("Digite o nome para cadastrar: ")
            face_db["names"].append(nome)
            face_db["encodings"].append(encoding)
            storage.save_faces(face_db)
            name = nome

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    return frame

if __name__ == '__main__':
    video.start_video_stream(process_frame)
