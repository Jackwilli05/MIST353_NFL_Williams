import streamlit as st
import pandas as pd
from fetch_data import fetch_data

def get_teams_with_logos_for_specified_fan_ui():
    st.header("Favorite Teams with Logos")
    
    email = st.text_input("Enter Fan Email", placeholder="e.g., tom.brady@example.com")
    
    if st.button("Get Teams"):
        if not email.strip():
            st.error("Please enter a fan email")
            return
        
        params = {"email": email.strip()}
        data = fetch_data("get_teams_for_specified_fan", params)
        
        if data and isinstance(data, list) and len(data) > 0:
            st.success(f"Found {len(data)} favorite teams for {email}")
            
            for team in data:
                st.subheader(team.get("TeamName", "Unknown Team"))
                st.write(f"City/State: {team.get('TeamCityState', 'N/A')}")
                st.write(f"Colors: {team.get('TeamColors', 'N/A')}")
                st.write(f"Conference: {team.get('Conference', 'N/A')}")
                st.write(f"Division: {team.get('Division', 'N/A')}")
                
                # Placeholder logo
                logo_url = f"https://placehold.co/100x100?text={team.get('TeamName', 'Team')[:3]}"
                st.image(logo_url, width=100)
                
                st.divider()
        else:
            st.info(f"No favorite teams found for {email}")