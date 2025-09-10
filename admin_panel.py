import streamlit as st
import yaml
from yaml.loader import SafeLoader
from yaml.dumper import SafeDumper

def admin_menu(config):
    st.subheader("User and permissions Management")
    users = list(config['credentials']['usernames'].keys())
    selected_user = st.selectbox("Select a user to manage", users)

    if selected_user:
        user_data = config['credentials']['usernames'][selected_user]
        st.write(f"Name: {user_data['name']}")
        st.write(f"Email: {user_data['email']}")

        available_roles = ['user', 'admin', 'root']
        current_role_idx = available_roles.index(user_data['role']) if user_data['role'] in available_roles else 0

        new_role = st.selectbox("Edit user profile",
                                available_roles,
                                index=current_role_idx,
                                key=f"role_{selected_user}" 
                                )
        
        if st.button(f"Update {selected_user}'s profile"):
            if selected_user == 'root' and new_role != 'root':
                st.error("Cannot edit root user's profile.")
            else:
                config['credentials']['usernames'][selected_user]['role'] = new_role

                try:
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, Dumper=SafeDumper, default_flow_style=False)
                    st.success(f"Updated {selected_user}'s role to {new_role}.")

                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to update config file: {e}")
