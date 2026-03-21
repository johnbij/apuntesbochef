import streamlit as st
from datetime import date

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

HABITOS_DEFAULT = [
    "🏃 Ejercicio",
    "📚 Estudiar 2h",
    "💧 Tomar agua",
    "😴 Dormir 8h",
    "🥗 Comer bien",
]

FRASES_INSPIRACION = [
    "El conocimiento es el arma más poderosa que puedes usar para cambiar el mundo. — Nelson Mandela",
    "La educación es el pasaporte hacia el futuro, porque el mañana pertenece a quienes se preparan hoy. — Malcolm X",
    "No cuentes los días, haz que los días cuenten. — Muhammad Ali",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día. — Robert Collier",
    "Primero, resuelve el problema. Luego, escribe el código. — John Johnson",
]

_DIAS_ES = [
    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo",
]
_MESES_ES = [
    "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]


def _fecha_es(d: date) -> str:
    """Retorna la fecha en español (p. ej. 'Sábado 21 de marzo de 2026')."""
    dia_semana = _DIAS_ES[d.weekday()]
    mes = _MESES_ES[d.month]
    return f"{dia_semana} {d.day} de {mes} de {d.year}"


def _frase_del_dia() -> str:
    idx = date.today().toordinal() % len(FRASES_INSPIRACION)
    return FRASES_INSPIRACION[idx]


# ---------------------------------------------------------------------------
# Secciones del dashboard
# ---------------------------------------------------------------------------

def _seccion_energia():
    st.markdown("### ⚡ Tracker de Energía y Ánimo")
    col1, col2 = st.columns(2)
    with col1:
        energia = st.slider("Nivel de energía", 1, 10, 7, key="dash_energia")
    with col2:
        animo = st.slider("Nivel de ánimo", 1, 10, 7, key="dash_animo")

    promedio = (energia + animo) / 2
    if promedio >= 7:
        emoji, msg = "🚀", "¡Vas con todo! Aprovecha este estado."
    elif promedio >= 4:
        emoji, msg = "😐", "Día regular. Un pequeño descanso puede ayudar."
    else:
        emoji, msg = "😴", "Cuídate. Descansa y vuelve con más fuerza."

    st.markdown(
        f"""
        <div style="background:#f0f2f6; border-radius:12px; padding:16px; text-align:center;">
            <span style="font-size:40px;">{emoji}</span>
            <p style="margin:8px 0 0;">{msg}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _seccion_habitos():
    st.markdown("### ✅ Log de Hábitos de Hoy")
    if "habitos_completados" not in st.session_state:
        st.session_state.habitos_completados = {h: False for h in HABITOS_DEFAULT}

    for habito in HABITOS_DEFAULT:
        checked = st.checkbox(
            habito,
            value=st.session_state.habitos_completados.get(habito, False),
            key=f"habit_{habito}",
        )
        st.session_state.habitos_completados[habito] = checked

    completados = sum(st.session_state.habitos_completados.values())
    total = len(HABITOS_DEFAULT)
    st.progress(completados / total, text=f"{completados}/{total} hábitos completados")


def _seccion_quick_capture():
    st.markdown("### 📝 Quick Capture")
    st.caption("Captura ideas rápidamente sin perder el hilo.")

    if "notas_rapidas" not in st.session_state:
        st.session_state.notas_rapidas = []

    nueva = st.text_input("Nueva nota:", placeholder="Escribe una idea…", key="qc_input")
    if st.button("➕ Guardar nota", key="qc_save") and nueva.strip():
        st.session_state.notas_rapidas.append(nueva.strip())
        st.rerun()

    if st.session_state.notas_rapidas:
        for i, nota in enumerate(reversed(st.session_state.notas_rapidas), 1):
            st.markdown(f"**{i}.** {nota}")
        if st.button("🗑️ Limpiar notas", key="qc_clear"):
            st.session_state.notas_rapidas = []
            st.rerun()
    else:
        st.info("Aún no hay notas guardadas.")


def _seccion_zen():
    st.markdown("### 🧘 Modo Zen")
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
            border-radius: 20px; padding: 40px 30px; text-align: center; color: white;
        ">
            <p style="font-size: 18px; opacity: 0.8;">✨ Frase del día</p>
            <p style="font-size: 20px; font-style: italic; line-height: 1.6;">
                "{_frase_del_dia()}"
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Entrada principal
# ---------------------------------------------------------------------------

def render_dashboard():
    """Renderiza el dashboard personal."""
    st.markdown("## 📊 Dashboard Personal")
    st.caption(f"📅 {_fecha_es(date.today())}")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["⚡ Energía", "✅ Hábitos", "📝 Quick Capture", "🧘 Zen"]
    )

    with tab1:
        _seccion_energia()
    with tab2:
        _seccion_habitos()
    with tab3:
        _seccion_quick_capture()
    with tab4:
        _seccion_zen()
