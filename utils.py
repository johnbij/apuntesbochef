import streamlit as st
from drive_utils import list_drive_uploads

def mostrar_seccion_ramo(nombre_ramo):
    """
    Lista archivos desde Google Drive y permite visualizarlos o descargarlos.
    Sincronizado con la cuenta de servicio bochefdrive.
    """
    st.markdown(f"### 📂 Material: {nombre_ramo.upper()}")
    
    # Intentamos listar desde la carpeta correspondiente en Drive
    archivos = list_drive_uploads(nombre_ramo)
    
    if archivos:
        for f in archivos:
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"📄 **{f['name']}**")
                with col2:
                    # Link de descarga directa usando el ID de Drive
                    url_descarga = f"https://drive.google.com/uc?export=download&id={f['id']}"
                    st.markdown(f"[⬇️ Descargar]({url_descarga})")
                
                # Visor embebido para PDFs (Requerimiento para M1)
                if f.get('mimeType') == 'application/pdf':
                    with st.expander(f"👁️ Vista previa: {f['name']}"):
                        pdf_url = f"https://drive.google.com/viewerng/viewer?embedded=true&url=https://drive.google.com/uc?export=view&id={f['id']}"
                        st.components.v1.iframe(pdf_url, height=600, scrolling=True)
                st.markdown("---")
    else:
        st.info(f"Aún no hay archivos disponibles en Drive para la sección {nombre_ramo}.")
