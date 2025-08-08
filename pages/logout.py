import streamlit as st
from Home_VirtuLab import menu
from Home_VirtuLab import header_img

header_img()

st.session_state.role = None

menu()