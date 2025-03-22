# Importer les bibliothèques nécessaires
import pickle
import json
import pandas as pd
import streamlit as st  # Ajout de l'import Streamlit

# Définir le modèle global en dehors des fonctions
modele_global = None

def model_pred(features):
    global modele_global  # Utiliser la variable globale directement
    test_data = pd.DataFrame([features])
    prediction = modele_global.predict(test_data)
    return int(prediction[0])

def charger_modele():
    global modele_global  # Utiliser la variable globale directement
    # Charger le modèle à partir du fichier Pickle avec un encodage spécifié
    with open('modele.pkl', 'rb') as fichier_modele:
        modele_global = pickle.load(fichier_modele)
    return modele_global

def charger_min_max():
    # Charger les valeurs min et max des caractéristiques depuis le fichier JSON avec un encodage spécifié
    with open('feature_min_max.json', 'r', encoding='utf-8') as json_file:
        min_max_dict_local = json.load(json_file)
    return min_max_dict_local

def charger_target_mapping():
    # Charger le mapping des targets depuis le fichier JSON avec un encodage spécifié
    with open('target_encoding.json', 'r', encoding='utf-8') as json_file:
        target_mapping_local = json.load(json_file)
    # Convertir les clés en entiers
    target_mapping_local = {int(key): value for key, value in target_mapping_local.items()}
    return target_mapping_local

# Charger les valeurs min et max
min_max_dict = charger_min_max()

# Interface utilisateur Streamlit
st.title("Load default prediction app")

# Créer des curseurs pour chaque caractéristique en utilisant les noms et
