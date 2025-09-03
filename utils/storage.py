import pickle
import os

def load_faces(filepath='data/faces.pkl'):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    return {"names": [], "encodings": []}

def save_faces(data, filepath='data/faces.pkl'):
    with open(filepath, 'wb') as f:
        pickle.dump(data, f)
