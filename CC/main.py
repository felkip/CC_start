import os
import sys

import streamlit as st

# Adicionar pasta ao path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.auth import login_user, register_user
from app.quiz import init_quiz_state, render_quiz, reset_quiz_state, iniciar_quiz
from app.roadmap import render_roadmap

# Configuração da página
st.set_page_config(
    page_title="CS Start",
    page_icon="🚀",
    layout="centered",
)

# Inicializar session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None

init_quiz_state()


# Página principal
st.title("🚀 CS Start")
st.markdown("Bem-vindo! Sua jornada em Ciência da Computação começa aqui.")

if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["Login", "Cadastro"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Usuário", key="login_username")
        password = st.text_input("Senha", type="password", key="login_password")

        if st.button("Entrar"):
            if username and password:
                success, user_id, message = login_user(username, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user_id
                    st.session_state.username = username
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Preencha todos os campos")

    with tab2:
        st.subheader("Criar Conta")
        new_username = st.text_input("Usuário", key="register_username")
        new_email = st.text_input("Email", key="register_email")
        new_password = st.text_input("Senha", type="password", key="register_password")
        confirm_password = st.text_input("Confirmar Senha", type="password", key="confirm_password")

        if st.button("Cadastrar"):
            if not (new_username and new_email and new_password):
                st.warning("Preencha todos os campos")
            elif new_password != confirm_password:
                st.warning("As senhas não coincidem")
            else:
                success, message = register_user(new_username, new_email, new_password)
                if success:
                    st.success(message)
                    st.info("Você pode fazer login agora!")
                else:
                    st.error(message)

else:
    st.success(f"Bem-vindo, {st.session_state.username}! 🎉")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Quiz de Perfil"):
            iniciar_quiz()

    with col2:
        if st.button("Ver Roadmap"):
            if "quiz_result" in st.session_state and st.session_state.quiz_result is not None:
                render_roadmap(st.session_state.quiz_result.get("profile"))
            else:
                st.info("Complete o quiz primeiro para ver o roadmap sugerido.")

    if st.button("Sair"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = None
        reset_quiz_state()
        st.rerun()

    render_quiz()

    if st.session_state.get("quiz_completed") and st.session_state.get("quiz_result") is not None:
        render_roadmap(st.session_state.quiz_result.get("profile"))
