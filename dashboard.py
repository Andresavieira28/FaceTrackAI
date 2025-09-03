# dashboard.py

import streamlit as st
import pickle
import os
from datetime import datetime

# Título da página
st.title("📊 Dashboard - FaceTrackAI")
st.subheader("Rostos reconhecidos pela webcam")

# Caminho para o arquivo de dados
DB_PATH = "data/recognized_faces.pkl"

# Função para carregar dados
def load_data():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "rb") as f:
            return pickle.load(f)
    return []

# Carrega os dados
registros = load_data()

# Exibe total de registros
st.info(f"Total de registros: {len(registros)}")

# Mostra os dados em uma tabela
if registros:
    st.table(registros)
else:
    st.warning("Nenhum rosto reconhecido ainda.")

# Filtro por nome
nomes = list(set([r["name"] for r in registros]))
nome_filtro = st.selectbox("Filtrar por nome:", ["Todos"] + nomes)

# Filtro aplicado
if nome_filtro != "Todos":
    filtrados = [r for r in registros if r["name"] == nome_filtro]
    st.write(f"Registros de **{nome_filtro}**: {len(filtrados)}")
    st.table(filtrados)

