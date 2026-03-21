import streamlit as st
from drive_utils import list_drive_uploads

def mostrar_seccion_ramo(nombre_ramo):
    """Lista archivos desde Google Drive y permite visualizarlos o descargarlos."""
    st.info(f"Cargando archivos de {nombre_ramo} desde Drive...")
    archivos = list_drive_uploads(nombre_ramo)
    
    if archivos:
        for f in archivos:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"📄 {f['name']}")
            with col2:
                # Link de descarga directa
                url_descarga = f"https://drive.google.com/uc?export=download&id={f['id']}"
                st.markdown(f"[⬇️ Descargar]({url_descarga})")
            
            # Visor embebido para PDFs
            if f['mimeType'] == 'application/pdf':
                with st.expander(f"👁️ Ver {f['name']}"):
                    pdf_url = f"https://drive.google.com/viewerng/viewer?embedded=true&url=https://drive.google.com/uc?export=view&id={f['id']}"
                    st.components.v1.iframe(pdf_url, height=600, scrolling=True)
            st.write("---")
    else:
        st.info(f"Aún no hay archivos en la carpeta de Drive para {nombre_ramo}.")
