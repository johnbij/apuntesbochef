import time
import os
import json
from collections import defaultdict
from datetime import datetime
import pytz
import streamlit as st
import streamlit.components.v1 as components

# Importaciones de tus utilidades de Drive y estilos
from drive_utils import upload_to_drive, list_drive_uploads, fetch_audio_bytes, list_gallery_images
from styles import apply_styles # Asumiendo que esta es la que configuramos antes
from mono_b64 import MONO_DATA_URI
from utils import download_button, mostrar_seccion_ramo 
from ejercicios_python import EJERCICIOS
from pomodoro import POMODORO_HTML
from gallery import render_gallery, render_drive_gallery

# =============================================================================
# 1. CONFIGURACIÓN Y ESTADOS
# =============================================================================

st.set_page_config(page_title="Ferran Files", page_icon="📚", layout="wide")

if "seccion" not in st.session_state:
    st.session_state.seccion = "recientes"
if "tema" not in st.session_state:
    st.session_state.tema = "claro"

# Configuración de Secciones de Drive
SECCIONES_DRIVE = {
    "ics111": "📘 ICS111",
    "ics161": "📗 ICS161",
    "mate10": "📐 MATE10",
    "apuntesbeuchef": "📝 Apuntes Beuchef"
}

GALLERY_SECTIONS = {
    "gal_ics111": "Fotos ICS111",
    "gal_ics161": "Fotos ICS161",
    "gal_mate10": "Fotos MATE10",
}

MAX_UPLOAD_BYTES = 100 * 1024 * 1024
DEFAULT_MIMETYPE = "application/octet-stream"

# =============================================================================
# 2. HEADER Y ESTILOS
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
# 3. BARRA DE NAVEGACIÓN (Layout de Botones)
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

st.markdown("---")

# =============================================================================
# 4. LÓGICA DE SUBIDA (Siempre visible arriba o en sección específica)
# =============================================================================
with st.expander("⬆️ Subir Archivos a Drive", expanded=False):
    seccion_label = st.selectbox("📍 Selecciona Destino:", options=list(SECCIONES_DRIVE.values()))
    # Invertir el dict para sacar la key
    dest_key = [k for k, v in SECCIONES_DRIVE.items() if v == seccion_label][0]
    
    uploaded_files = st.file_uploader("Arrastra aquí tus archivos", accept_multiple_files=True)
    if uploaded_files and st.button("📤 Confirmar Subida"):
        for f in uploaded_files:
            mimetype = f.type or DEFAULT_MIMETYPE
            success = upload_to_drive(f.read(), f.name, mimetype, folder_name=dest_key)
            if success: st.success(f"✅ {f.name} subido.")
            else: st.error(f"❌ Error en {f.name}")
        st.rerun()

# =============================================================================
# 5. RENDERIZADO DE CONTENIDO
# =============================================================================

sec = st.session_state.seccion

# --- SECCIONES DE RAMOS Y BEUCHEF ---
if sec in SECCIONES_DRIVE.keys():
    st.subheader(f"📑 {SECCIONES_DRIVE[sec]}")
    mostrar_seccion_ramo(sec)

# --- RECIENTES ---
elif sec == "recientes":
    st.subheader("📥 Archivos Recién Subidos")
    archivos = list_drive_uploads()
    if archivos:
        for f in archivos:
            col_a, col_b = st.columns([4, 1])
            col_a.write(f"📄 {f['name']}")
            url = f"https://drive.google.com/uc?export=download&id={f['id']}"
            col_b.markdown(f"[⬇️ Descargar]({url})")
    else:
        st.info("No hay archivos nuevos.")

# --- GALERÍAS ---
elif sec == "galerias":
    st.subheader("📸 Galerías de Fotos")
    gcol = st.columns(3)
    if gcol[0].button("Fotos ICS111"): st.session_state.seccion = "gal_ics111"
    if gcol[1].button("Fotos ICS161"): st.session_state.seccion = "gal_ics161"
    if gcol[2].button("Fotos MATE10"): st.session_state.seccion = "gal_mate10"

elif sec in GALLERY_SECTIONS:
    course_key = sec.replace("gal_", "")
    all_imgs = list_gallery_images()
    filtered = [img for img in all_imgs if img.get("folder", "").lower() == course_key]
    render_drive_gallery(filtered, GALLERY_SECTIONS[sec])
