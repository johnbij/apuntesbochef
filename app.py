import streamlit as st
from datetime import datetime
import pytz

from contenidos import CONTENIDOS
from styles import aplicar_estilos

# =============================================================================
# 1. CONFIGURACIÓN Y ESTADOS
# =============================================================================

st.set_page_config(page_title="El Hub de los K", page_icon="🐉", layout="wide")

if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
if 'ir_a_pdf'           not in st.session_state: st.session_state.ir_a_pdf           = False
if 'bienvenida_vista'   not in st.session_state: st.session_state.bienvenida_vista   = False

COLORES = {
    "rojo":    "#c0392b",
    "verde":   "#1b5e20",
    "morado":  "#7b1fa2",
    "naranja": "#e65100",
}

# =============================================================================
# 2. ESTILOS
# =============================================================================

aplicar_estilos()

# =============================================================================
# 3. BARRA LATERAL
# =============================================================================

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Bij**")
    st.divider()
    menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# =============================================================================
# 4. DASHBOARD PRINCIPAL
# =============================================================================

if menu == "🏠 Dashboard":

    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)

    st.markdown(
        f'<div class="header-azul">'
        f'<div class="titulo-header">🐉 Hub de los K. Materiales en PDF</div>'
        f'<div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # ── PANTALLA INICIAL ─────────────────────────────────────────────────────
    if st.session_state.eje_actual is None:
        
        # CSS individual para cada botón de eje
        st.markdown("""
        <style>
        div.eje-n div.stButton > button { background-color: #c0392b !important; color: white !important; border: none !important; }
        div.eje-a div.stButton > button { background-color: #1b5e20 !important; color: white !important; border: none !important; }
        div.eje-g div.stButton > button { background-color: #7b1fa2 !important; color: white !important; border: none !important; }
        div.eje-d div.stButton > button { background-color: #e65100 !important; color: white !important; border: none !important; }
        </style>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="eje-n">', unsafe_allow_html=True)
            if st.button("🔢 DIM",   key="m_n", use_container_width=True):
                st.session_state.eje_actual = "🔢 DIM"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="eje-a">', unsafe_allow_html=True)
            if st.button("📉 DFI",   key="m_a", use_container_width=True):
                st.session_state.eje_actual = "📉 DFI"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="eje-g">', unsafe_allow_html=True)
            if st.button("📐 DII", key="m_g", use_container_width=True):
                st.session_state.eje_actual = "📐 DII"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="eje-d">', unsafe_allow_html=True)
            if st.button("📊 DCC", key="m_d", use_container_width=True):
                st.session_state.eje_actual = "📊 DCC"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # ── DENTRO DE UN EJE ────────────────────────────────────────────────────
    else:
        # CSS para barra de navegación con colores por eje
        st.markdown("""
        <style>
        div.nav-n div.stButton > button { background-color: #c0392b !important; color: white !important; border: none !important; }
        div.nav-a div.stButton > button { background-color: #1b5e20 !important; color: white !important; border: none !important; }
        div.nav-g div.stButton > button { background-color: #7b1fa2 !important; color: white !important; border: none !important; }
        div.nav-d div.stButton > button { background-color: #e65100 !important; color: white !important; border: none !important; }
        div.nav-home div.stButton > button { background-color: #1a1a2e !important; color: white !important; border: none !important; }
        </style>
        """, unsafe_allow_html=True)

        n_cols = st.columns(5)
        with n_cols[0]:
            st.markdown('<div class="nav-home">', unsafe_allow_html=True)
            if st.button("🏠", key="n_h", use_container_width=True):
                st.session_state.eje_actual      = None
                st.session_state.subcat_actual   = None
                st.session_state.clase_seleccionada = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with n_cols[1]:
            st.markdown('<div class="nav-n">', unsafe_allow_html=True)
            if st.button("DIM", key="n_n", use_container_width=True):
                st.session_state.eje_actual      = "🔢 DIM"
                st.session_state.subcat_actual   = None
                st.session_state.clase_seleccionada = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with n_cols[2]:
            st.markdown('<div class="nav-a">', unsafe_allow_html=True)
            if st.button("DFI", key="n_a", use_container_width=True):
                st.session_state.eje_actual      = "📉 DFI"
                st.session_state.subcat_actual   = None
                st.session_state.clase_seleccionada = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with n_cols[3]:
            st.markdown('<div class="nav-g">', unsafe_allow_html=True)
            if st.button("DII", key="n_g", use_container_width=True):
                st.session_state.eje_actual      = "📐 DII"
                st.session_state.subcat_actual   = None
                st.session_state.clase_seleccionada = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with n_cols[4]:
            st.markdown('<div class="nav-d">', unsafe_allow_html=True)
            if st.button("DCC", key="n_d", use_container_width=True):
                st.session_state.eje_actual      = "📊 DCC"
                st.session_state.subcat_actual   = None
                st.session_state.clase_seleccionada = None
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("---")

        # ── NAVEGACIÓN ───────────────────────────────────────────────────────
        eje      = st.session_state.eje_actual
        eje_data = CONTENIDOS.get(eje, {})
        subcats  = eje_data.get("subcategorias", {})
        color    = COLORES.get(eje_data.get("color_subcats", "rojo"), "#c0392b")

        # NIVEL 1: subcategorías
        if st.session_state.subcat_actual is None:
            st.markdown(f"## {eje}")
            st.markdown(f"""
            <style>
            button[kind="primary"], div.stButton > button[data-testid="baseButton-primary"] {{
                background-color: {color} !important;
                color: white !important;
                border: none !important;
                border-radius: 12px !important;
                min-height: 75px !important;
                font-size: 17px !important;
                font-weight: bold !important;
                width: 100% !important;
                margin-bottom: 6px !important;
            }}
            </style>
            """, unsafe_allow_html=True)
            for nombre_subcat in subcats.keys():
                if st.button(nombre_subcat, key=f"sc_{nombre_subcat}",
                             use_container_width=True, type="primary"):
                    st.session_state.subcat_actual = nombre_subcat
                    st.rerun()

        # NIVEL 2: lista de clases
        elif st.session_state.clase_seleccionada is None:
            subcat = st.session_state.subcat_actual
            clases = subcats.get(subcat, {})
            st.subheader(f"{eje} › {subcat}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            for codigo, datos in clases.items():
                if st.button(datos["label"], key=f"cls_{codigo}", use_container_width=True):
                    st.session_state.clase_seleccionada = codigo
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("🔙 Volver", key="volver_subcat"):
                st.session_state.subcat_actual = None
                st.rerun()

        # NIVEL 3: contenido
        else:
            subcat  = st.session_state.subcat_actual
            codigo  = st.session_state.clase_seleccionada
            clase   = subcats.get(subcat, {}).get(codigo)

            # Calcular anterior / siguiente
            codigos  = list(subcats.get(subcat, {}).keys())
            idx      = codigos.index(codigo)
            anterior = codigos[idx - 1] if idx > 0 else None
            siguiente = codigos[idx + 1] if idx < len(codigos) - 1 else None

            # CSS para los botones de navegación con color del eje
            st.markdown(f"""
            <style>
            .nav-clase div.stButton > button {{
                background-color: {color} !important;
                color: white !important;
                border: none !important;
                border-radius: 10px !important;
                min-height: 60px !important;
                font-size: 14px !important;
                font-weight: bold !important;
                width: 100% !important;
            }}
            </style>
            """, unsafe_allow_html=True)

            def barra_navegacion(sufijo):
                st.markdown('<div class="nav-clase">', unsafe_allow_html=True)
                col_ant, col_volver, col_sig = st.columns([2, 1, 2])
                with col_ant:
                    if anterior:
                        label_ant = subcats[subcat][anterior]["label"]
                        if st.button(f"← {label_ant}", key=f"btn_anterior_{sufijo}", use_container_width=True):
                            st.session_state.clase_seleccionada = anterior
                            st.rerun()
                with col_volver:
                    if st.button("📋", key=f"volver_lista_{sufijo}", use_container_width=True, help="Volver al listado"):
                        st.session_state.clase_seleccionada = None
                        st.rerun()
                with col_sig:
                    if siguiente:
                        label_sig = subcats[subcat][siguiente]["label"]
                        if st.button(f"{label_sig} →", key=f"btn_siguiente_{sufijo}", use_container_width=True):
                            st.session_state.clase_seleccionada = siguiente
                            st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            # Barra ARRIBA (entre header y clase)
            barra_navegacion("top")
            st.write("---")

            # Contenido de la clase
            if clase:
                clase["render"]()
            else:
                st.warning(f"Clase {codigo} no encontrada.")

            # Barra ABAJO
            st.write("---")
            barra_navegacion("bot")

elif menu == "🐉 Bienvenida":
    st.markdown("""
    <style>
    .bienvenida-hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        padding: 50px 30px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    .bienvenida-dragon { font-size: 80px; margin-bottom: 10px; }
    .bienvenida-titulo { font-size: 36px; font-weight: 900; letter-spacing: 2px; margin-bottom: 8px; }
    .bienvenida-lema {
        font-size: 20px;
        color: #f0c040;
        font-style: italic;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .bienvenida-sub { font-size: 15px; opacity: 0.8; max-width: 500px; margin: 0 auto; }

    .card-eje {
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 10px;
    }

    .seccion-titulo {
        font-size: 22px;
        font-weight: bold;
        color: #1a1a2e;
        border-left: 5px solid #c0392b;
        padding-left: 12px;
        margin: 30px 0 15px 0;
    }

    .pill {
        display: inline-block;
        background: #f0f0f0;
        border-radius: 20px;
        padding: 6px 16px;
        margin: 4px;
        font-size: 14px;
        color: #333;
    }
    </style>

    <div class="bienvenida-hero">
        <div class="bienvenida-dragon">🐉</div>
        <div class="bienvenida-titulo">HUB de los K</div>
        <div class="bienvenida-lema">"8====D"</div>
        <div class="bienvenida-sub">
          Full apuntes.<br>
            Pa que pasí tus cagas de ramos.
        </div>
    </div>
    """, unsafe_allow_html=True)


    # CTA
    st.write("")
    col_iz, col_cta, col_der = st.columns([1, 2, 1])
    with col_cta:
        if st.button("🚀 Ir al Dashboard", key="cta_dashboard", use_container_width=True):
            st.session_state.bienvenida_vista = True
            st.success("¡Usa el menú lateral para ir al Dashboard PAES! 👈")
