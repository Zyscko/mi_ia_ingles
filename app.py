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
    # Cambiamos el texto aburrido por el tuyo:
    st.warning("Si esto no le sirve pues no moleste crjo") 
    st.markdown("---")

# --- CUERPO PRINCIPAL ---
st.title("🎙️ Lector de Voz Natural Pro")
texto_usuario = st.text_area("Escribe lo que quieras que la IA diga:", 
                            placeholder="Escribe aquí...", height=150)

# Función para generar el audio
async def generate_voice(text):
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    await communicate.save("audio.mp3")

if st.button("📢 Generar Voz Natural"):
    if texto_usuario:
        with st.spinner("Generando..."):
            try:
                asyncio.run(generate_voice(texto_usuario))
                st.audio("audio.mp3")
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Escribe algo primero, Emmanuel.")