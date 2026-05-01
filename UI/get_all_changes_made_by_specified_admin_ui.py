import streamlit as st
import pandas as pd
from fetch_data import fetch_data

def get_all_changes_made_by_specified_admin_ui():
    st.header("Changes Made by NFL Admin")
    
    if not st.session_state.get("is_authenticated", False):
        st.warning("Please login to view change history")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can view change history")
        return
    
    admin_name = st.session_state.get("app_user_fullname", "Admin")
    admin_id = st.session_state.get("app_user_id", 1)
    
    st.info(f"Logged in as: {admin_name} (ID: {admin_id})")
    
    if st.button("Get My Changes"):
        with st.spinner("Loading changes..."):
            params = {"nfl_admin_id": admin_id}
            data = fetch_data("get_all_changes_made_by_specified_admin", params)
            
            if data and isinstance(data, list) and len(data) > 0:
                st.success(f"Found {len(data)} changes")
                df = pd.DataFrame(data)
                
                # Rename columns for better display
                column_rename = {
                    "ChangeDateTime": "Date/Time",
                    "ChangeType": "Type",
                    "ChangeDescription": "Description",
                    "GameRound": "Round",
                    "GameDate": "Game Date",
                    "GameStartTime": "Start Time",
                    "HomeTeam": "Home Team",
                    "AwayTeam": "Away Team",
                    "StadiumName": "Stadium"
                }
                df = df.rename(columns=column_rename)
                
                st.dataframe(df, use_container_width=True, hide_index=True)
                
                # Download button
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download as CSV",
                    data=csv,
                    file_name=f"admin_changes_{admin_id}.csv",
                    mime="text/csv"
                )
            else:
                st.info(f"No changes found for {admin_name}")