import streamlit as st
from fetch_data import fetch_data

def validate_user_ui():
    st.header("Validate User")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Validate User"):
        input_params = {}
        
        if not email.strip():
            st.error("Email is required.")
        else:
            input_params["email"] = email.strip()

        if not password.strip():
            st.error("Password is required.")
        else:
            input_params["password"] = password.strip()

        if email.strip() and password.strip():
            result = fetch_data("validate_user", input_params, method="POST")

            # Check if result is a list (successful validation)
            if isinstance(result, list) and len(result) > 0:
                st.subheader(f"User {email} is valid:")
                st.dataframe(result, use_container_width=True, hide_index=True)
            # Check if result is a dict with an error or message
            elif isinstance(result, dict):
                if "error" in result:
                    st.error(result["error"])
                elif "message" in result:
                    st.info(result["message"])
                else:
                    st.info(f"User {email} is not valid. Please check the inputs and try again.")
            else:
                st.info(f"User {email} is not valid. Please check the inputs and try again.")