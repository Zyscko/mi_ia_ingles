import streamlit as st
import asyncio
import edge_tts
import os

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="IA de Voz Natural - Emmanuel", page_icon="🎙️")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("⭐ Creador")
    st.success("Emmanuel")
    st.write("Esta versión usa voces de Microsoft Edge (Naturales y Gratuitas).")
    st.markdown("---")

# --- CUERPO PRINCIPAL ---
st.title("🎙️ Lector de Voz Natural Pro")
texto_usuario = st.text_area("Escribe lo que quieras que la IA diga:", 
                            placeholder="Ej: Hello Emmanuel, this voice sounds much more human!", 
                            height=150)

# Función para generar el audio (esta parte es técnica pero necesaria)
async def generate_voice(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural") # Voz natural masculina
    await communicate.save("audio.mp3")

if st.button("📢 Generar Voz Natural"):
    if texto_usuario:
        with st.spinner("Generando audio con acento natural..."):
            try:
                # Ejecutamos la generación de voz
                asyncio.run(generate_voice(texto_usuario))
                
                # Reproducimos en la web
                st.audio("audio.mp3")
                st.success("¡Listo! Escucha la diferencia en la entonación.")
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Escribe algo primero, Emmanuel.")