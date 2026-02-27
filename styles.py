import streamlit as st


def aplicar_estilos():
    st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* --- BARRA DE NAVEGACIÓN 🏠 / N / A / G / D --- */
    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 70px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background-color: #1a1a2e !important;
        color: white !important;
        border: none !important;
    }

    /* --- BOTONES DE LISTA DE CLASES --- */
    .cat-container div.stButton > button {
        min-height: 75px !important; border-radius: 12px !important; margin-bottom: 10px !important;
        width: 100% !important; font-size: 17px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* --- BOTÓN PDF --- */
    .pdf-btn div.stButton > button {
        background-color: #4a0e8f !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* --- CRONÓMETRO --- */
    .crono-digital {
        font-family: 'Courier New', monospace;
        font-size: 35px;
        font-weight: bold;
        color: #3b71ca;
        text-align: center;
        width: 100%;
        display: block;
    }
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
