
import os
import streamlit as st

def list_pdfs(folder_path):
    """Lista todos los archivos PDF en una carpeta específica."""
    if not os.path.exists(folder_path):
        return []
    return [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

def download_button(file_path, file_name):
    """Genera un botón de descarga para un archivo."""
    try:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label=f"📥 {file_name}",
            data=pdf_bytes,
            file_name=file_name,
            mime="application/pdf",
            key=file_path 
        )
    except Exception as e:
        st.error(f"Error al cargar {file_name}")

def mostrar_seccion_ramo(nombre_ramo):
    """Automatiza la búsqueda y despliegue de PDFs en la sección correspondiente."""
    path_ramo = f"pdfs/{nombre_ramo}"
    pdfs = list_pdfs(path_ramo)
    
    if pdfs:
        for archivo in pdfs:
            ruta_completa = os.path.join(path_ramo, archivo)
            download_button(ruta_completa, archivo)
    else:
        st.info(f"Aún no hay archivos en {nombre_ramo}.")
