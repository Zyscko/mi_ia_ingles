import streamlit as st
import requests

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="IA de Voz - Emmanuel", page_icon="🎙️")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("⭐ Creador")
    st.success("Emmanuel")
    st.write("Esta IA usa el modelo Multilingual v2 para una voz humana perfecta.")
    st.markdown("---")
    st.caption("© 2026 - Powered by ElevenLabs")

# --- CUERPO PRINCIPAL ---
st.title("🎙️ Lector de Voz Pro")
st.markdown("##### Escribe lo que quieras y la IA lo dirá con acento y pausas naturales.")

texto_usuario = st.text_area("Escribe tu texto aquí:", 
                            placeholder="Ej: Hello, my name is Emmanuel and this is my first AI project.", 
                            height=150)

if st.button("📢 Generar Voz"):
    if texto_usuario:
        with st.spinner("Generando audio ultra-realista..."):
            API_KEY = "sk_0e3d808de424936e3f10b1bf15093c163e512cd54871ec62" 
            VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Voz de Rachel
            
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": API_KEY
            }
            # CAMBIO AQUÍ: Usamos 'eleven_multilingual_v2' que es el modelo actual
            data = {
                "text": texto_usuario,
                "model_id": "eleven_multilingual_v2", 
                "voice_settings": {
                    "stability": 0.5, 
                    "similarity_boost": 0.8
                }
            }

            try:
                response = requests.post(url, json=data, headers=headers)
                if response.status_code == 200:
                    with open("audio.mp3", "wb") as f:
                        f.write(response.content)
                    st.audio("audio.mp3")
                    st.success("¡Audio generado con éxito!")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Escribe algo primero, Emmanuel.")