import streamlit as st
from Home_VirtuLab import menu
from Home_VirtuLab import header_img

header_img()

st.title("IEEE RAS UFCG - Virtual Lab")

st.sidebar.title("Navigation")

# if not st.session_state.role:
if "role" not in st.session_state:
    st.session_state.role = None

st.session_state.role = st.session_state.role

def set_role():
    st.session_state.role = st.session_state.role

st.selectbox(
    "Select your role",
    [None, "user", "admin", "super-user"],
    key="role",
    on_change= set_role,
    )

menu()
# else:
    # menu()
