import streamlit as st
from Home_VirtuLab import menu_with_redirect
from Home_VirtuLab import header_img

header_img()

menu_with_redirect()

st.title("This is the Default User Page")
st.markdown(f"You are currently logged in with the role: **{st.session_state.role}**")

st.session_state.role = st.session_state.role