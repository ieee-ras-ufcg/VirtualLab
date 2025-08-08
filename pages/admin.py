import streamlit as st
from Home_VirtuLab import menu_with_redirect
from Home_VirtuLab import header_img

header_img()

menu_with_redirect()

if st.session_state.role not in ["admin", "super-user"]:
    st.warning("You do not have permission to access this page.")
    st.stop()

st.title("User Management")
st.markdown("This page is for managing users. Only accessible by admins and superusers.")
st.markdown(f"You are currently logged in with the role: **{st.session_state.role}**")

st.session_state.role = st.session_state.role