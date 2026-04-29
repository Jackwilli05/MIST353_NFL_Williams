import streamlit as st
from fetch_data import fetch_data

def validate_user_ui():
    st.header("Validate User")
    
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):
        if not email.strip() or not password.strip():
            st.error("Email and Password are required.")
            return
        
        result = fetch_data("validate_user", {"email": email.strip(), "password": password.strip()}, method="POST")

        if result and isinstance(result, list) and len(result) > 0:
            # Store user info in session state
            st.session_state.app_user_id = result[0]["AppUserID"]
            st.session_state.app_user_fullname = result[0]["Fullname"]
            st.session_state.user_role = result[0]["UserRole"]
            st.session_state.is_authenticated = True
            st.success(f"Welcome {st.session_state.app_user_fullname}!")
            st.rerun()
        else:
            st.error("Invalid email or password")

    # Show logged in status
    if st.session_state.get("is_authenticated", False):
        st.divider()
        st.info(f"Logged in as: {st.session_state.app_user_fullname} ({st.session_state.user_role})")
        
        if st.button("Logout"):
            for key in ["app_user_id", "app_user_fullname", "user_role", "is_authenticated"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()