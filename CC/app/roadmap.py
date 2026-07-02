try:
    import streamlit as st
except ModuleNotFoundError:  # pragma: no cover - fallback para testes simples
    class _StreamlitFallback:
        def info(self, *args, **kwargs):
            return None

        def markdown(self, *args, **kwargs):
            return None

        def subheader(self, *args, **kwargs):
            return None

        def write(self, *args, **kwargs):
            return None

    st = _StreamlitFallback()

ROADMAPS = {
    "programming": [
        "Fundamentos de lógica",
        "Variáveis e estruturas básicas",
        "Funções",
        "Estruturas de decisão e repetição",
        "Introdução à programação com Python",
    ],
    "tech": [
        "Fundamentos de computadores",
        "Internet e sistemas",
        "Ferramentas básicas de produtividade",
        "Introdução a bancos de dados",
        "Noções de segurança e uso de tecnologia",
    ],
    "beginner": [
        "Introdução à computação",
        "Conceitos básicos de tecnologia",
        "Primeiros passos em lógica",
        "Pequenos exercícios práticos",
        "Estudo guiado com ritmo leve",
    ],
}


def get_roadmap_for_profile(profile):
    return ROADMAPS.get(profile, ROADMAPS["beginner"])


def render_roadmap(profile=None):
    if profile is None:
        profile = st.session_state.get("quiz_result", {}).get("profile")

    if profile is None:
        st.info("Complete o quiz para ver um roadmap sugerido.")
        return

    topics = get_roadmap_for_profile(profile)

    st.markdown("---")
    st.subheader("🗺️ Roadmap de Estudos")
    st.write("Baseado no seu perfil, aqui estão os próximos passos:")

    for index, topic in enumerate(topics, start=1):
        st.write(f"{index}. {topic}")
