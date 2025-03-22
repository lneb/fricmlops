# Importer les bibliothèques nécessaires
import pickle
import json
import numpy as np
import pandas as pd
import streamlit as st  # Ajout de l'import Streamlit

# Fonction pour prédire à partir du modèle
def model_pred(features, modele):
    test_data = pd.DataFrame([features])
    prediction = modele.predict(test_data)
    return int(prediction[0])

# Charger le modèle à partir du fichier Pickle
def charger_modele():
    with open("modele.pkl", "rb") as fichier_modele:
        modele = pickle.load(fichier_modele)
    return modele

# Charger les valeurs min et max des caractéristiques depuis le fichier JSON
def charger_min_max():
    with open("feature_min_max.json", "r", encoding="utf-8") as json_file:
        min_max_dict_local = json.load(json_file)
    return min_max_dict_local

# Charger le mapping des targets depuis le fichier JSON
def charger_target_mapping():
    with open("target_encoding.json", "r", encoding="utf-8") as json_file:
        target_mapping_local = json.load(json_file)
    # Convertir les clés en entiers
    target_mapping_local = {
        int(key): value for key, value in target_mapping_local.items()
    }
    return target_mapping_local

# Charger les valeurs min et max
min_max_dict = charger_min_max()

# Interface utilisateur Streamlit
st.title("Load default prediction app")

# Créer des curseurs pour chaque caractéristique en utilisant les noms et valeurs depuis le JSON
caracteristiques_entree = []
for feature, limits in min_max_dict.items():
    caracteristique = st.slider(
        f"{feature}",
        float(limits["min"]),
        float(limits["max"]),
        float((limits["min"] + limits["max"]) / 2),
    )
    caracteristiques_entree.append(caracteristique)

# Charger le modèle et le mapping de la cible
modele = charger_modele()  # Charger le modèle une seule fois
target_mapping = charger_target_mapping()

# Préparer les caractéristiques pour la prédiction
caracteristiques = np.array([caracteristiques_entree])

# Prévoir la classe avec le modèle
prediction_encoded = modele.predict(caracteristiques)

# Décoder la prédiction
prediction_decoded = target_mapping[prediction_encoded[0]]

# Afficher la prédiction
st.markdown(
    f"<p style='font-size:24px; font-weight:bold;'>Load default prediction value: {prediction_decoded}</p>",
    unsafe_allow_html=True,
)
