import re
import streamlit as st


def extraer_id_drive(url: str) -> str | None:
    """Extrae el ID de un archivo o carpeta de Google Drive a partir de su URL."""
    patrones = [
        r"/file/d/([a-zA-Z0-9_-]+)",
        r"id=([a-zA-Z0-9_-]+)",
        r"/folders/([a-zA-Z0-9_-]+)",
        r"open\?id=([a-zA-Z0-9_-]+)",
    ]
    for patron in patrones:
        match = re.search(patron, url)
        if match:
            return match.group(1)
    return None


def url_directa_imagen(file_id: str) -> str:
    """Convierte un ID de archivo de Drive en una URL de descarga directa (para imágenes)."""
    return f"https://drive.google.com/uc?export=view&id={file_id}"


def url_preview_pdf(file_id: str) -> str:
    """Genera la URL de previsualización de un PDF alojado en Google Drive."""
    return f"https://drive.google.com/file/d/{file_id}/preview"


def embed_pdf_drive(url_o_id: str, height: int = 700):
    """Renderiza un PDF de Google Drive dentro de un iframe de Streamlit."""
    file_id = extraer_id_drive(url_o_id) if "/" in url_o_id else url_o_id
    if not file_id:
        st.error("URL de Google Drive no válida.")
        return
    preview_url = url_preview_pdf(file_id)
    st.components.v1.iframe(preview_url, height=height, scrolling=True)


def embed_imagen_drive(url_o_id: str, caption: str = "", use_container_width: bool = True):
    """Muestra una imagen alojada en Google Drive."""
    file_id = extraer_id_drive(url_o_id) if "/" in url_o_id else url_o_id
    if not file_id:
        st.error("URL de Google Drive no válida.")
        return
    img_url = url_directa_imagen(file_id)
    st.image(img_url, caption=caption, use_container_width=use_container_width)
