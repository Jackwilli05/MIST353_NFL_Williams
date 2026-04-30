import streamlit as st
import requests

FASTAPI_URL = "https://mist353-api-williams.azurewebsites.net"

def validate_user_ui():
    st.header("Validate User")
    
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if not email.strip() or not password.strip():
            st.error("Email and Password are required.")
            return
        
        # Send as query parameters for GET request
        params = {
            "email": email.strip(),
            "password": password.strip()
        }
        
        try:
            response = requests.get(f"{FASTAPI_URL}/validate_user", params=params)
            
            if response.status_code == 200:
                data = response.json()
                if data and isinstance(data, list) and len(data) > 0:
                    st.session_state.app_user_id = data[0]["AppUserID"]
                    st.session_state.app_user_fullname = data[0]["Fullname"]
                    st.session_state.user_role = data[0]["UserRole"]
                    st.session_state.is_authenticated = True
                    st.success(f"Welcome {st.session_state.app_user_fullname}!")
                    st.rerun()
                else:
                    st.error("Invalid email or password")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")

    if st.session_state.get("is_authenticated", False):
        st.divider()
        st.info(f"Logged in as: {st.session_state.app_user_fullname} ({st.session_state.user_role})")
        
        if st.button("Logout"):
            for key in ["app_user_id", "app_user_fullname", "user_role", "is_authenticated"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()