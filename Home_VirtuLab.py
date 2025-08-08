import streamlit as st
import numpy as np

# menu for authenticated users

def header_img():
    st.image("virtulogo.png", width=2500)

def authenticated_menu():
    st.sidebar.image("virtulogo.png", width=200) 
    st.sidebar.page_link("pages/user.py", label="User Profile")
    if st.session_state.role in ["admin", "super-user"]:
        st.sidebar.page_link("pages/admin.py", label="User Management")
        st.sidebar.page_link(
            "pages/super-user.py",
            label="Manage Admin Access",
            disabled=st.session_state.role != "super-user",
        )
    if "role" in st.session_state:
        st.sidebar.page_link("pages/logout.py", label="Log out")
def unauthenticated_menu():
    st.sidebar.image("virtulogo.png", width=200)
    st.sidebar.page_link("app.py", label="Login")

def menu():
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
        return
    menu()

st.sidebar.markdown("")