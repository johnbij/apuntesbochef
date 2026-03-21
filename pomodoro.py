import streamlit as st
import time

try:
    from streamlit_autorefresh import st_autorefresh  # type: ignore
    _HAS_AUTOREFRESH = True
except ImportError:
    _HAS_AUTOREFRESH = False

DURACION_TRABAJO_SEG = 25 * 60
DURACION_DESCANSO_SEG = 5 * 60


def _formatear_tiempo(segundos: int) -> str:
    minutos, segs = divmod(max(0, segundos), 60)
    return f"{minutos:02d}:{segs:02d}"


def render_pomodoro():
    """Renderiza el temporizador Pomodoro interactivo."""
    st.markdown("## 🍅 Temporizador Pomodoro")
    st.caption("25 minutos de trabajo · 5 minutos de descanso")

    # Inicializar estados
    if "pomo_activo" not in st.session_state:
        st.session_state.pomo_activo = False
    if "pomo_modo" not in st.session_state:
        st.session_state.pomo_modo = "trabajo"
    if "pomo_inicio" not in st.session_state:
        st.session_state.pomo_inicio = None
    if "pomo_sesiones" not in st.session_state:
        st.session_state.pomo_sesiones = 0

    duracion = DURACION_TRABAJO_SEG if st.session_state.pomo_modo == "trabajo" else DURACION_DESCANSO_SEG
    modo_label = "🔴 Trabajo" if st.session_state.pomo_modo == "trabajo" else "🟢 Descanso"

    # Calcular tiempo restante
    if st.session_state.pomo_activo and st.session_state.pomo_inicio:
        transcurrido = int(time.time() - st.session_state.pomo_inicio)
        restante = duracion - transcurrido
        if restante <= 0:
            st.session_state.pomo_activo = False
            if st.session_state.pomo_modo == "trabajo":
                st.session_state.pomo_sesiones += 1
                st.session_state.pomo_modo = "descanso"
            else:
                st.session_state.pomo_modo = "trabajo"
            st.session_state.pomo_inicio = None
            restante = 0
            st.rerun()
    else:
        restante = duracion

    # Mostrar reloj digital
    st.markdown(
        f"""
        <div style="
            font-family: 'Courier New', monospace;
            font-size: 72px;
            font-weight: bold;
            color: {'#c0392b' if st.session_state.pomo_modo == 'trabajo' else '#1b5e20'};
            text-align: center;
            padding: 20px 0;
        ">{_formatear_tiempo(restante)}</div>
        <div style="text-align:center; font-size: 20px; margin-bottom: 16px;">{modo_label}</div>
        """,
        unsafe_allow_html=True,
    )

    # Botones de control
    col1, col2, col3 = st.columns(3)
    with col1:
        if not st.session_state.pomo_activo:
            if st.button("▶️ Iniciar", key="pomo_start", use_container_width=True):
                st.session_state.pomo_activo = True
                st.session_state.pomo_inicio = time.time()
                st.rerun()
        else:
            if st.button("⏸️ Pausar", key="pomo_pause", use_container_width=True):
                st.session_state.pomo_activo = False
                st.session_state.pomo_inicio = None
                st.rerun()
    with col2:
        if st.button("⏹️ Reiniciar", key="pomo_reset", use_container_width=True):
            st.session_state.pomo_activo = False
            st.session_state.pomo_inicio = None
            st.session_state.pomo_modo = "trabajo"
            st.rerun()
    with col3:
        if st.button("⏭️ Saltar", key="pomo_skip", use_container_width=True):
            st.session_state.pomo_activo = False
            st.session_state.pomo_inicio = None
            if st.session_state.pomo_modo == "trabajo":
                st.session_state.pomo_sesiones += 1
                st.session_state.pomo_modo = "descanso"
            else:
                st.session_state.pomo_modo = "trabajo"
            st.rerun()

    st.markdown("---")
    st.metric("🍅 Sesiones completadas hoy", st.session_state.pomo_sesiones)

    # Auto-refresco mientras el temporizador está activo
    if st.session_state.pomo_activo:
        if _HAS_AUTOREFRESH:
            st_autorefresh(interval=1000, key="pomo_autorefresh")
        else:
            time.sleep(1)
            st.rerun()
