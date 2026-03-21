import streamlit as st

# ---------------------------------------------------------------------------
# Definición de temas
# ---------------------------------------------------------------------------

TEMAS = {
    "claro": {
        "header_bg": "#3b71ca",
        "header_text": "white",
        "btn_primary": "#3b71ca",
        "btn_text": "white",
        "accent": "#3b71ca",
        "bg": "#FAFAFA",
        "secondary_bg": "#F0F2F6",
    },
    "oscuro": {
        "header_bg": "#1a1a2e",
        "header_text": "white",
        "btn_primary": "#16213e",
        "btn_text": "white",
        "accent": "#6C63FF",
        "bg": "#0f0f23",
        "secondary_bg": "#1a1a2e",
    },
    "azul": {
        "header_bg": "#0d47a1",
        "header_text": "white",
        "btn_primary": "#1565c0",
        "btn_text": "white",
        "accent": "#42a5f5",
        "bg": "#e3f2fd",
        "secondary_bg": "#bbdefb",
    },
    "rosado": {
        "header_bg": "#ad1457",
        "header_text": "white",
        "btn_primary": "#c2185b",
        "btn_text": "white",
        "accent": "#f48fb1",
        "bg": "#fce4ec",
        "secondary_bg": "#f8bbd0",
    },
}


def aplicar_estilos(tema: str = "claro"):
    """Aplica los estilos globales de la aplicación.

    Parámetros
    ----------
    tema : str
        Nombre del tema a aplicar: ``"claro"``, ``"oscuro"``, ``"azul"`` o ``"rosado"``.
        Si el tema no existe, se usa ``"claro"`` como fallback.
    """
    t = TEMAS.get(tema, TEMAS["claro"])
    header_bg = t["header_bg"]

    st.markdown(f"""
    <style>
    .header-azul {{ background-color: {header_bg}; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }}
    .titulo-header {{ font-size: 20px; font-weight: bold; margin-bottom: 5px; }}
    .info-header {{ font-size: 14px; opacity: 0.9; }}
    .header-rojo {{ background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }}
    .timer-item {{ font-size: 16px; font-weight: bold; }}

    /* --- BARRA DE NAVEGACIÓN 🏠 / N / A / G / D --- */
    [data-testid="stHorizontalBlock"] {{ display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }}
    [data-testid="stHorizontalBlock"] > div {{ flex: 1 1 0% !important; min-width: 0 !important; }}
    [data-testid="stHorizontalBlock"] button {{
        width: 100% !important;
        min-height: 70px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background-color: #1a1a2e !important;
        color: white !important;
        border: none !important;
    }}

    /* --- BOTONES DE LISTA DE CLASES --- */
    .cat-container div.stButton > button {{
        min-height: 75px !important; border-radius: 12px !important; margin-bottom: 10px !important;
        width: 100% !important; font-size: 17px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }}

    /* --- BOTÓN PDF --- */
    .pdf-btn div.stButton > button {{
        background-color: #4a0e8f !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }}

    /* --- CRONÓMETRO --- */
    .crono-digital {{
        font-family: 'Courier New', monospace;
        font-size: 35px;
        font-weight: bold;
        color: {header_bg};
        text-align: center;
        width: 100%;
        display: block;
    }}
    </style>
    """, unsafe_allow_html=True)


def css_boton_subcat(key, color_hex):
    """Inyecta CSS justo antes del botón usando su key como selector aria-label."""
    st.markdown(f"""
    <style>
    button[kind="secondary"][data-testid="baseButton-secondary"]:has(+ *),
    div.stButton:has(> button[aria-label="{key}"]) > button,
    div.stButton > button[title="{key}"] {{
        background-color: {color_hex} !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 75px !important;
        font-size: 17px !important;
        font-weight: bold !important;
        width: 100% !important;
        margin-bottom: 10px !important;
    }}
    </style>
    """, unsafe_allow_html=True)
