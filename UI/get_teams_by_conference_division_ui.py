import streamlit as st
from fetch_data import fetch_data

def get_teams_by_conference_division_ui():
    st.header("Get Teams by Conference and Division")
    
    conference = st.text_input("Conference")
    division = st.text_input("Division")
    
    if st.button("Fetch Teams"):
        input_params = {}
        if conference:
            input_params["conference"] = conference
        if division:
            input_params["division"] = division
        
        df = fetch_data("get_teams_by_conference_division", input_params)
        
        if df:
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No teams found")