import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from yaml.dumper import SafeDumper
import os
from dotenv import load_dotenv

from Home_VirtuLab import menu
from Home_VirtuLab import header_img

load_dotenv()
#header_img()

st.set_page_config(page_title="Virtual Lab", layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Load auth configs

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    os.getenv('COOKIE_SIGNATURE_KEY'),
    config['cookie']['expiry_days']
)

# Login section

login_tab, register_tab = st.tabs(["Login", "Register"])

with login_tab:
    name, auth_status, username = authenticator.login('Login', 'main')

with register_tab:
    try:
        if authenticator.register_user('Register user', pre_authorized=config['preauthorized']['emails']):
            config['credentials']['usernames'][st.session_state['username']]['role'] = 'user'

            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, Dumper=SafeDumper, default_flow_style=False)

            st.success('User registered successfully')
    except Exception as e:
        st.error(e)


if st.session_state.get("authentication_status"):
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f"Welcome, {name}")
    
    st.session_state['role'] = config['credentials']['usernames'][username]['role']
    st.session_state['username'] = username

    st.title("Virtual Lab Homepage")
    st.write("This is the homepage of the Virtual Lab application. Select an option from the sidebar to get started.")

    if st.session_state['role'] == 'root':
        from admin_panel import admin_menu
        with st.sidebar.expander("Admin Panel"):
            admin_menu(config)
    
    st.header("Main Dashboard")
    #todo: Add main dashboard content

elif auth_status is False:
    st.error('Username/password is incorrect')
elif auth_status is None:
    st.warning('Please enter your username and password')