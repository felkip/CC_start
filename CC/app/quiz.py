import streamlit as st

QUESTIONS = [
    {
        "pergunta": "O que mais te atrai em tecnologia?",
        "opcoes": [
            {"texto": "Criar soluções e programas", "valor": "programming"},
            {"texto": "Explorar ferramentas e novidades", "valor": "tech"},
            {"texto": "Entender o básico com calma", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Quando encontra um problema, o que costuma fazer?",
        "opcoes": [
            {"texto": "Tentar resolver logicamente", "valor": "programming"},
            {"texto": "Buscar formas novas de lidar com ele", "valor": "tech"},
            {"texto": "Pedir ajuda e aprender passo a passo", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Você gosta mais de:",
        "opcoes": [
            {"texto": "Pensar em algoritmos e estrutura", "valor": "programming"},
            {"texto": "Testar apps e produtos digitais", "valor": "tech"},
            {"texto": "Aprender fundamentos primeiro", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Como prefere aprender algo novo?",
        "opcoes": [
            {"texto": "Com exercícios práticos", "valor": "programming"},
            {"texto": "Com exemplos modernos e tecnológicos", "valor": "tech"},
            {"texto": "Com explicações simples e repetição", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "O que te inspira mais?",
        "opcoes": [
            {"texto": "Construir algo do zero", "valor": "programming"},
            {"texto": "Ver novas ideias ganhando forma", "valor": "tech"},
            {"texto": "Crescer com passos pequenos", "valor": "beginner"},
        ],
    },
]


def init_quiz_state():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_completed" not in st.session_state:
        st.session_state.quiz_completed = False
    if "quiz_step" not in st.session_state:
        st.session_state.quiz_step = 0
    if "quiz_scores" not in st.session_state:
        st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    if "quiz_result" not in st.session_state:
        st.session_state.quiz_result = None
    if "quiz_answer" not in st.session_state:
        st.session_state.quiz_answer = None


def iniciar_quiz():
    init_quiz_state()
    st.session_state.quiz_started = True
    st.session_state.quiz_completed = False
    st.session_state.quiz_step = 0
    st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    st.session_state.quiz_result = None
    st.session_state.quiz_answer = None


def reset_quiz_state():
    init_quiz_state()
    st.session_state.quiz_started = False
    st.session_state.quiz_completed = False
    st.session_state.quiz_step = 0
    st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    st.session_state.quiz_result = None
    st.session_state.quiz_answer = None


def calcular_result(scores):
    perfil = max(scores, key=scores.get)
    resultados = {
        "programming": {
            "titulo": "Perfil de Programação",
            "descricao": "Você tende a gostar de resolver problemas, pensar logicamente e criar soluções.",
            "profile": "programming",
        },
        "tech": {
            "titulo": "Perfil de Tecnologia",
            "descricao": "Você se interessa por ferramentas, inovação e por explorar o universo tecnológico.",
            "profile": "tech",
        },
        "beginner": {
            "titulo": "Perfil de Início",
            "descricao": "Você está começando e pode evoluir com passos simples, práticos e bem guiados.",
            "profile": "beginner",
        },
    }
    return resultados[perfil]


def render_quiz():
    init_quiz_state()

    if not st.session_state.quiz_started:
        st.info("Responda a algumas perguntas para descobrir seu perfil inicial em tecnologia.")
        return

    st.markdown("---")
    st.subheader("🧠 Quiz de Perfil")

    if not st.session_state.quiz_completed:
        total_perguntas = len(QUESTIONS)
        pergunta_atual = QUESTIONS[st.session_state.quiz_step]
        progresso = (st.session_state.quiz_step + 1) / total_perguntas

        st.progress(progresso)
        st.write(f"**Pergunta {st.session_state.quiz_step + 1} de {total_perguntas}**")
        st.write(pergunta_atual["pergunta"])

        resposta = st.radio(
            "Escolha uma opção:",
            [opcao["texto"] for opcao in pergunta_atual["opcoes"]],
            key="quiz_answer",
        )

        if st.button("Próxima pergunta" if st.session_state.quiz_step < total_perguntas - 1 else "Ver resultado"):
            if resposta:
                opcao_escolhida = next(
                    opcao for opcao in pergunta_atual["opcoes"] if opcao["texto"] == resposta
                )
                st.session_state.quiz_scores[opcao_escolhida["valor"]] += 1

                if st.session_state.quiz_step < total_perguntas - 1:
                    st.session_state.quiz_step += 1
                    st.session_state.quiz_answer = None
                    st.rerun()
                else:
                    st.session_state.quiz_completed = True
                    st.session_state.quiz_result = calcular_result(st.session_state.quiz_scores)
                    st.session_state.quiz_answer = None
                    st.rerun()
            else:
                st.warning("Selecione uma opção para continuar.")
    else:
        st.success("Quiz concluído!")
        st.subheader(st.session_state.quiz_result["titulo"])
        st.write(st.session_state.quiz_result["descricao"])

        st.caption("Seu resultado é uma primeira indicação de perfil. Pode ser ajustado conforme você avança nos estudos.")

        if st.button("Fazer outro quiz"):
            iniciar_quiz()
            st.rerun()
