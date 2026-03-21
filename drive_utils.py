import os
import json
import io
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# Configuración de IDs de carpetas en Google Drive
FOLDER_IDS = {
    "ics111": "ID_DE_TU_CARPETA_ICS111",
    "ics161": "ID_DE_TU_CARPETA_ICS161",
    "mate10": "ID_DE_TU_CARPETA_MATE10",
    "apuntesbeuchef": "ID_DE_TU_CARPETA_BEUCHEF", # Carpeta nueva
    "recientes": "ID_DE_TU_CARPETA_RECIENTES"
}

def get_drive_service():
    """Autenticación con Google Drive usando Secrets de Streamlit."""
    try:
        if "textkey" not in st.secrets:
            st.error("No se encontró 'textkey' en los Secrets de Streamlit.")
            return None
        creds_dict = json.loads(st.secrets["textkey"])
        creds = service_account.Credentials.from_service_account_info(creds_dict)
        return build('drive', 'v3', credentials=creds)
    except Exception as e:
        st.error(f"Error de autenticación: {e}")
        return None

def upload_to_drive(file_bytes, file_name, mimetype, folder_name="recientes"):
    """Sube un archivo a una carpeta específica de Google Drive."""
    service = get_drive_service()
    if not service: return False
    
    folder_id = FOLDER_IDS.get(folder_name, FOLDER_IDS["recientes"])
    file_metadata = {'name': file_name, 'parents': [folder_id]}
    
    # Uso correcto de MediaIoBaseUpload para evitar el error anterior
    fh = io.BytesIO(file_bytes)
    media = MediaIoBaseUpload(fh, mimetype=mimetype, resumable=True)
    
    try:
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return True
    except Exception as e:
        st.error(f"Error al subir {file_name}: {e}")
        return False

def list_drive_uploads(folder_name="recientes"):
    """Lista los archivos de una carpeta específica."""
    service = get_drive_service()
    if not service: return []
    
    folder_id = FOLDER_IDS.get(folder_name, FOLDER_IDS["recientes"])
    query = f"'{folder_id}' in parents and trashed = false"
    
    results = service.files().list(q=query, fields="files(id, name, mimeType)").execute()
    return results.get('files', [])

def fetch_audio_bytes(file_id):
    return None

def list_gallery_images():
    return []
