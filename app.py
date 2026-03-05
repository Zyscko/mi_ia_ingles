import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Configuración de la interfaz
st.set_page_config(page_title="Mi IA de Inglés", page_icon="🎙️")
st.title("🎙️ Traductor y Coach de Pronunciación")
st.markdown("Pega tu texto y yo lo adaptaré al inglés con pronunciación perfecta.")

# 1. Entrada de texto
texto_usuario = st.text_area("Escribe o pega aquí el texto en español:", placeholder="Ej: Hola, ¿cómo va todo?")

if st.button("Adaptar y Escuchar"):
    if texto_usuario:
        # 2. Traducción Adaptativa
        # Usamos GoogleTranslator pero configurado para ser natural
        traduccion = GoogleTranslator(source='auto', target='en').translate(texto_usuario)
        
        st.subheader("Adaptación al Inglés:")
        st.success(traduccion)

        # 3. Generar la Voz (TTS)
        # 'en' es inglés, 'tld=com' usa el acento estándar americano
        tts = gTTS(text=traduccion, lang='en', tld='com')
        tts.save("audio.mp3")

        # 4. Reproducir en la interfaz
        st.subheader("Escucha la pronunciación:")
        audio_file = open("audio.mp3", "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        
        # Limpieza (opcional)
        audio_file.close()
    else:
        st.warning("Por favor, escribe algo primero.")
        