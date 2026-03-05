import streamlit as st
from deep_translator import GoogleTranslator
import requests

# --- CONFIGURACIÓN DE ESTILO ---
st.set_page_config(page_title="English Coach Pro", page_icon="🎙️", layout="centered")

# CSS para que se vea más moderno
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #ff4b4b; color: white; }
    .stTextArea>div>div>textarea { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (Sidebar) ---
with st.sidebar:
    st.title("⭐ Panel de Control")
    st.info("Esta IA adapta tus frases para que suenen naturales en Estados Unidos, no como un traductor de libro.")
    st.markdown("---")
    st.write("🚀 **Desarrollado por:**")
    st.success("Emmanuel") # Solo tu nombre, sin el correo
    st.caption("Versión 2.0 | 2026")

# --- CUERPO PRINCIPAL ---
st.image("https://images.unsplash.com/photo-1543165796-5426273ea4d2?auto=format&fit=crop&q=80&w=1000", use_container_width=True)
st.title("🎙️ English Coach Pro")
st.markdown("##### *Habla como un nativo, no como un robot.*")

# Entrada de texto
texto_usuario = st.text_area("¿Qué quieres decir en inglés hoy?", 
                            placeholder="Escribe aquí en español...", height=150)

# Espaciado
st.write("")

if st.button("✨ ¡Convertir a Voz Realista!"):
    if texto_usuario:
        col1, col2 = st.columns(2)
        
        with st.spinner("Procesando..."):
            # 1. Traducción Natural
            traduccion = GoogleTranslator(source='es', target='en').translate(texto_usuario)
            
            with col1:
                st.markdown("### 📝 Tu frase adaptada:")
                st.info(traduccion)

            # 2. Voz de ElevenLabs
            API_KEY = "Tsk_0e3d808de424936e3f10b1bf15093c163e512cd54871ec62" 
            VOICE_ID = "21m00Tcm4TlvDq8ikWAM"