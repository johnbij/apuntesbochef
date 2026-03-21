import time
import os
import json
from collections import defaultdict
from datetime import datetime
import pytz
import streamlit as st
import streamlit.components.v1 as components

# 1. IMPORTACIONES DE TUS MÓDULOS (Con manejo de errores para evitar caídas)
try:
    from drive_utils import upload_to_drive, list_drive_uploads, fetch_audio_bytes, list_gallery_images
    from styles import apply_styles
    from utils import mostrar_seccion_ramo 
    from ejercicios_python import EJERCICIOS
    from pomodoro import render_pomodoro
    from gallery import render_drive_gallery
except ImportError as e:
    st.error(f"Error importando módulos: {e}")
    st.stop()

# =============================================================================
# 2. CONFIGURACIÓN Y ESTADOS
# =============================================================================

st.set_page_config(page_title="Ferran Files", page_icon="🚀", layout="wide")

if "seccion" not in st.session_state:
    st.session_state.seccion = "recientes"
if "tema" not in st.session_state:
    st.session_state.tema = "claro"

# Diccionarios de configuración (Aquí estaba el SyntaxError, asegúrate de las llaves)
SECCIONES_DRIVE = {
    "ics111": "📘 ICS111",
    "ics161": "📗 ICS161",
    "mate10": "📐 MATE10",
    "apuntesbeuchef": "📝 Apuntes Beuchef"
}

GALLERY_SECTIONS = {
    "gal_ics111": "Fotos ICS111",
    "gal_ics161": "Fotos ICS161",
    "gal_mate10": "Fotos MATE10"
}

MAX_UPLOAD_BYTES = 100 * 1024 * 1024
DEFAULT_MIMETYPE = "application/octet-stream"

# =============================================================================
# 3. HEADER Y ESTILOS
# =============================================================================
apply_styles()

zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)

st.markdown(
    f'<div style="background-color:#1a1a2e; padding:20px; border-radius:10px; color:white; text-align:center; margin-bottom:20px;">'
    f'<h1 style="margin:0;">🚀 Ferran Files</h1>'
    f'<p style="margin:0;">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</p>'
    f'</div>',
    unsafe_allow_html=True
)

# =============================================================================
# 4. BARRA DE NAVEGACIÓN
# =============================================================================
col_nav = st.columns(6)
with col_nav[0]: 
    if st.button("📥 Recientes"): st.session_state.seccion = "recientes"
with col_nav[1]: 
    if st.button("📘 ICS111"): st.session_state.seccion = "ics111"
with col_nav[2]: 
    if st.button("📗 ICS161"): st.session_state.seccion = "ics161"
with col_nav[3]: 
    if st.button("📐 MATE10"): st.session_state.seccion = "mate10"
with col_nav[4]: 
    if st.button("📝 Beuchef"): st.session_state.seccion = "apuntesbeuchef"
with col_nav[5]: 
    if st.button("🖼️ Galerías"): st.session_state.seccion = "galerias"

st.write("---")

# =============================================================================
# 5. LÓGICA DE RENDERIZADO
# =============================================================================

sec = st.session_state.seccion

# --- SECCIONES DE RAMOS Y BEUCHEF ---
if sec in SECCIONES_DRIVE:
    st.subheader(f"📑 {SECCIONES_DRIVE[sec]}")
    mostrar_seccion_ramo(sec)

# --- RECIENTES (CON SUBIDA) ---
elif sec == "recientes":
    st.subheader("⬆️ Subir Archivos a Drive")
    dest_label = st.selectbox("📍 Selecciona Destino:", options=list(SECCIONES_DRIVE.values()))
    dest_key = [k for k, v in SECCIONES_DRIVE.items() if v == dest_label][0]
    
    uploaded_files = st.file_uploader("Sube material aquí", accept_multiple_files=True)
    if uploaded_files and st.button("📤 Confirmar Subida"):
        for f in uploaded_files:
            upload_to_drive(f.read(), f.name, f.type or DEFAULT_MIMETYPE, folder_name=dest_key)
        st.success("¡Archivos subidos!")
        st.rerun()

# --- GALERÍAS ---
elif sec == "galerias":
    st.subheader("📸 Galerías")
    gcol = st.columns(3)
    if gcol[0].button("Fotos ICS111"): st.session_state.seccion = "gal_ics111"
    if gcol[1].button("Fotos ICS161"): st.session_state.seccion = "gal_ics161"
    if gcol[2].button("Fotos MATE10"): st.session_state.seccion = "gal_mate10"

elif sec in GALLERY_SECTIONS:
    course_key = sec.replace("gal_", "")
    all_imgs = list_gallery_images()
    filtered = [img for img in all_imgs if img.get("folder", "").lower() == course_key]
    render_drive_gallery(filtered, GALLERY_SECTIONS[sec])
