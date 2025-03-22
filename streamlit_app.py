# Importer les bibliothèques nécessaires
import pickle
import json

import pandas as pd
# import streamlit as st  # Ajout de l'import Streamlit

# Fonction pour prédire à partir du modèle
def model_pred(features, modele):
    test_data = pd.DataFrame([features])
    prediction = modele.predict(test_data)
    return int(prediction[0])

# Charger le modèle à partir du fichier Pickle
def charger_modele():
    with open('modele.pkl', 'rb') as fichier_modele:
        modele = pickle.load(fichier_modele)
    return modele

# Charger les valeurs min et max des caractéristiques depuis le fichier JSON
def charger_min_max():
    with open('feature_min_max.json', 'r', encoding='utf-8') as json_file:
        min_max_dict_local = json.load(json_file)
    return min_max_dict_local

# Charger le mapping des targets depuis le fichier JSON
def charger_target_
