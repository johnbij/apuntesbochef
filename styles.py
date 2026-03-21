import streamlit as st

def aplicar_estilos(tema="claro"):
    """
    Configura la apariencia visual del Hub. 
    Sincronizado con app.py para evitar errores de importación.
    """
    
    # Definición de colores según el tema
    if tema == "oscuro":
        bg_color = "#0e1117"
        text_color = "#ffffff"
        header_bg = "#1a1a2e"
    elif tema == "azul":
        bg_color = "#e3f2fd"
        text_color = "#0d47a1"
        header_bg = "#1565c0"
    elif tema == "rosado":
        bg_color = "#fce4ec"
        text_color = "#880e4f"
        header_bg = "#ad1457"
    else:  # tema claro
        bg_color = "#ffffff"
        text_color = "#1a1a2e"
        header_bg = "#3b71ca"

    st.markdown(f"""
    <style>
    /* Configuración Base */
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}

    /* Header Principal */
    .header-azul {{
        background-color: {header_bg};
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    
    .titulo-header {{
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }}

    /* Botones de Navegación del Hub */
    div.stButton > button {{
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        border: 1px solid rgba(0,0,0,0.1) !important;
    }}

    div.stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }}

    /* Estilos específicos para secciones de Beuchef/Ramos */
    .cat-container {{
        background-color: rgba(255,255,255,0.05);
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid {header_bg};
    }}

    /* Visor de PDF embebido */
    iframe {{
        border: 2px solid {header_bg};
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Alias para evitar el error 'cannot import name apply_styles'
def apply_styles(tema="claro"):
    aplicar_estilos(tema)
