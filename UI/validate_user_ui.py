import streamlit as st
from fetch_data import fetch_data

def validate_user_ui():
    st.header("Validate User")
    
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password", type="password")

    if st.button("Validate User"):
        if not email.strip() or not password.strip():
            st.error("Email and Password are required.")
            return
        
        result = fetch_data("validate_user", {"email": email.strip(), "password": password.strip()}, method="POST")

        if result and isinstance(result, list) and len(result) > 0:
            # Store user info in session state
            st.session_state.app_user_id = result[0]["AppUserID"]
            st.session_state.app_user_fullname = result[0]["Fullname"]
            st.session_state.is_authenticated = True
            st.success(f"Welcome {st.session_state.app_user_fullname}!")
        else:
            st.error("Invalid email or password")

    # Show fan's teams after login
    if st.session_state.get("is_authenticated", False):
        st.divider()
        st.subheader(f"Teams associated with {st.session_state.app_user_fullname}")
        
        # Fetch fan's favorite teams
        fan_data = fetch_data("get_teams_for_specified_fan", {"email": email.strip()}, method="GET")
        
        if fan_data and isinstance(fan_data, list) and len(fan_data) > 0:
            # Add placeholder columns for Start Time and Venue if not in data
            for team in fan_data:
                if "StartTime" not in team:
                    team["StartTime"] = "TBD"
                if "Venue" not in team:
                    team["Venue"] = "TBD"
            
            st.dataframe(fan_data, use_container_width=True, hide_index=True)
        else:
            st.info("No teams associated with this fan yet.")
        
        # Show fan ID
        st.text_input("Fan ID", value=st.session_state.app_user_id, disabled=True)