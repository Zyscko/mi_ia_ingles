import streamlit as st
from deep_translator import GoogleTranslator
import requests

# --- CONFIGURACIÓN Y CRÉDITOS ---
st.set_page_config(page_title="IA de Inglés - Emmanuel", page_icon="🇺🇸")

st.sidebar.title("🚀 Creador")
st.sidebar.write("**Nombre:** Emmanuel")
st.sidebar.write("**Email:** samuelcuesta911@gmail.com")
st.sidebar.markdown("---")

# --- INTERFAZ ---
st.title("🎙️ English Coach Pro")
texto_usuario = st.text_area("Escribe en español:")

if st.button("Adaptar y Generar Voz Realista"):
    if texto_usuario:
        # Traducción
        traduccion = GoogleTranslator(source='es', target='en').translate(texto_usuario)
        st.success(f"**Traducción:** {traduccion}")

        # Voz Humana (ElevenLabs)
        # Pega tu clave de la imagen image_902565.png aquí abajo:
        API_KEY = "sk_0e3d808de424936e3f10b1bf15093c163e512cd54871ec62" 
        VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Voz natural de Rachel
        
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": API_KEY}
        data = {"text": traduccion, "model_id": "eleven_monolingual_v1", "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            with open("audio.mp3", "wb") as f:
                f.write(response.content)
            st.audio("audio.mp3")
        else:
            st.error("Revisa tu API Key de ElevenLabs")