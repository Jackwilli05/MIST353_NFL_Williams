import streamlit as st
from fetch_data import fetch_data

def get_teams_for_specified_fan_ui():
    st.header("Get Favorite Teams for Specified Fan")
    
    email = st.text_input("Enter Fan's Email", placeholder="e.g., tom.brady@example.com")
    
    if st.button("Get Favorite Teams"):
        if not email.strip():
            st.error("Email is required.")
            return
        
        result = fetch_data("get_teams_for_specified_fan", {"email": email.strip()}, method="GET")
        
        if result and isinstance(result, list) and len(result) > 0:
            st.success(f"Found {len(result)} favorite teams for {email}")
            st.dataframe(result, use_container_width=True, hide_index=True)
        elif isinstance(result, dict) and "message" in result:
            st.info(result["message"])
        else:
            st.info(f"No favorite teams found for {email}")