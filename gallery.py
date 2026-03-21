import streamlit as st
from drive_utils import url_directa_imagen, extraer_id_drive


MAX_GALLERY_COLUMNS = 4


def render_galeria(imagenes: list[dict], columnas: int = 3):
    """
    Renderiza una galería responsiva de imágenes.

    Parámetros
    ----------
    imagenes : list[dict]
        Lista de dicts con claves:
          - ``url``     : URL de Google Drive o URL directa
          - ``caption`` : (opcional) texto descriptivo
    columnas : int
        Número de columnas de la galería (1-4).
    """
    if not imagenes:
        st.info("No hay imágenes para mostrar en esta galería.")
        return

    columnas = max(1, min(columnas, MAX_GALLERY_COLUMNS))
    cols = st.columns(columnas)

    for idx, item in enumerate(imagenes):
        url = item.get("url", "")
        caption = item.get("caption", "")

        # Intentar obtener URL directa si es un enlace de Drive
        file_id = extraer_id_drive(url)
        img_url = url_directa_imagen(file_id) if file_id else url

        with cols[idx % columnas]:
            st.image(img_url, caption=caption, use_container_width=True)


def render_galeria_section(titulo: str, imagenes: list[dict], columnas: int = 3):
    """Renderiza una sección con título y galería."""
    st.markdown(f"### {titulo}")
    render_galeria(imagenes, columnas=columnas)
