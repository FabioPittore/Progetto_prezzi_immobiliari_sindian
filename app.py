import streamlit as st
import pandas as pd
import joblib
import os

# Carica il modello OLS salvato
model_path = os.path.join("Modello", "model_ols.joblib")
model_ols = joblib.load(model_path)

# Limiti geografici
lat_min, lat_max = 24.93, 25.08
lon_min, lon_max = 121.47, 121.57

st.title("Stima del prezzo immobiliare al metro quadro in dollari taiwanesi (NT$/m²) - Sindian, Nuova Taipei, Taiwan")

latitude = st.number_input("Inserisci la latitudine", value=25.0)
longitude = st.number_input("Inserisci la longitudine", value=121.5)

if latitude < lat_min or latitude > lat_max:
    st.error(f"⚠️ Latitudine fuori dai limiti del dataset! ({lat_min} - {lat_max})")
elif longitude < lon_min or longitude > lon_max:
    st.error(f"⚠️ Longitudine fuori dai limiti del dataset! ({lon_min} - {lon_max})")
else:
    # Costruzione input per il modello
    input_data = pd.DataFrame([{
        "const": 1,
        "X5 latitude": latitude,
        "X6 longitude": longitude
    }])[["const", "X5 latitude", "X6 longitude"]]

    prediction = model_ols.predict(input_data)[0]

    prezzo_formattato = f"{prediction:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    st.success(f"💰 Prezzo stimato: {prezzo_formattato} NT€/m²")
