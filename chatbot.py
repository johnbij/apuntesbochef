import streamlit as st

SYSTEM_PROMPT = (
    "Eres un asistente académico especializado en ingeniería y ciencias. "
    "Ayudas a estudiantes con dudas de matemáticas, física, programación y otras materias. "
    "Responde siempre en español, de forma clara y concisa."
)


def _get_client():
    """Inicializa el cliente de Google Gemini usando la clave almacenada en secrets."""
    try:
        from google import genai  # type: ignore
        api_key = st.secrets.get("GEMINI_API_KEY", "")
        if not api_key:
            return None, "⚠️ Configura `GEMINI_API_KEY` en `.streamlit/secrets.toml` para usar el chatbot."
        client = genai.Client(api_key=api_key)
        return client, None
    except ImportError:
        return None, "⚠️ Instala `google-genai` para usar el chatbot: `pip install google-genai`."


def render_chatbot():
    """Renderiza el asistente IA con Google Gemini."""
    st.markdown("## 🤖 Asistente Académico IA")
    st.caption("Powered by Google Gemini · Consultas sobre matemáticas, física, programación y más.")

    client, error = _get_client()
    if error:
        st.warning(error)
        st.stop()

    # Historial de conversación en session_state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar historial
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Entrada del usuario
    if prompt := st.chat_input("Escribe tu pregunta académica…"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Pensando…"):
                try:
                    # Construir historial en formato Gemini
                    contents = []
                    for msg in st.session_state.chat_history:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append({"role": role, "parts": [{"text": msg["content"]}]})

                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=contents,
                        config={"system_instruction": SYSTEM_PROMPT},
                    )
                    reply = response.text
                except Exception as exc:
                    reply = f"❌ Error al contactar Gemini: {exc}"

                st.markdown(reply)
                st.session_state.chat_history.append({"role": "assistant", "content": reply})

    # Botón para limpiar el historial
    if st.session_state.chat_history:
        if st.button("🗑️ Limpiar conversación", key="chat_clear"):
            st.session_state.chat_history = []
            st.rerun()
