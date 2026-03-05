import streamlit as st
import requests

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="IA de Voz - Emmanuel", page_icon="🎙️")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("⭐ Creador")
    st.success("Emmanuel")
    st.write("Esta IA leerá exactamente lo que escribas con una voz humana profesional.")

# --- CUERPO PRINCIPAL ---
st.title("🎙️ Lector de Voz Pro")
texto_usuario = st.text_area("Escribe el texto que quieres que la IA diga:", 
                            placeholder="Escribe aquí...", height=150)

if st.button("📢 Generar Voz"):
    if texto_usuario:
        with st.spinner("Generando audio..."):
            # Configuración de ElevenLabs
            # ¡IMPORTANTE! Pega tu clave de la imagen image_902565.png abajo:
            API_KEY = "sk_0e3d808de424936e3f10b1bf15093c163e512cd54871ec62" 
            VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Voz de Rachel
            
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": API_KEY
            }
            data = {
                "text": texto_usuario,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
            }

            try:
                response = requests.post(url, json=data, headers=headers)
                if response.status_code == 200:
                    with open("audio.mp3", "wb") as f:
                        f.write(response.content)
                    st.audio("audio.mp3")
                    st.success("¡Audio generado con éxito!")
                else:
                    st.error(f"Error {response.status_code}: Revisa tu API Key de ElevenLabs.")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
    else:
        st.warning("Escribe algo primero.")