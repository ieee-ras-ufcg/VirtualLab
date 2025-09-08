import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
from dotenv import load_dotenv

from Home_VirtuLab import menu
from Home_VirtuLab import header_img

load_dotenv()
#header_img()

st.set_page_config(page_title="Virtual Lab", layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    os.getenv('COOKIE_SIGNATURE_KEY'),
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, auth_status, username = authenticator.login('Login', 'main')

if auth_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f"Welcome, {name}")
    st.session_state['role'] = config['credentials']['usernames'][username]['role']
    st.session_state['username'] = username