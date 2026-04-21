import streamlit as st
from fetch_data import fetch_data

def get_teams_for_specified_fan_ui():
    st.header("Get Favorite Teams for Specified Fan")
    
    email = st.text_input("Enter Fan Email", placeholder="e.g., tom.brady@example.com")
    
    if st.button("Get Favorite Teams"):
        if not email.strip():
            st.error("Please enter a fan email.")
            return
        
        input_params = {"email": email.strip()}
        data = fetch_data("get_teams_for_specified_fan", input_params)
        
        if data and isinstance(data, list) and len(data) > 0:
            st.success(f"Found {len(data)} favorite teams for {email}")
            st.dataframe(data, use_container_width=True, hide_index=True)
        elif isinstance(data, dict) and "message" in data:
            st.info(data["message"])
        else:
            st.info(f"No favorite teams found for {email}")