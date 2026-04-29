import streamlit as st
import requests

FASTAPI_URL = "https://mist353-api-williams.azurewebsites.net"

def schedule_game_ui():
    st.header("Schedule a New Game")
    
    # Check if user is logged in as NFL Admin
    if not st.session_state.get("is_authenticated", False):
        st.warning("Please login as NFL Admin to schedule games")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
        return
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')} (NFL Admin)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        home_team_id = st.number_input("Home Team ID", min_value=1, max_value=32, step=1, help="Team ID 1-32")
        game_round = st.selectbox("Game Round", ["Wild Card", "Divisional", "Conference", "Super Bowl"])
        game_date = st.date_input("Game Date")
        stadium_id = st.number_input("Stadium ID", min_value=1, step=1)
    
    with col2:
        away_team_id = st.number_input("Away Team ID", min_value=1, max_value=32, step=1, help="Team ID 1-32")
        game_start_time = st.time_input("Game Start Time")
        nfl_admin_id = st.number_input("NFL Admin ID", min_value=1, step=1, value=st.session_state.get("app_user_id", 1))
    
    if st.button("Schedule Game", type="primary"):
        # Validate home and away teams are different
        if home_team_id == away_team_id:
            st.error("Home team and away team cannot be the same")
            return
        
        payload = {
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_round": game_round,
            "game_date": str(game_date),
            "game_start_time": str(game_start_time),
            "stadium_id": stadium_id,
            "nfl_admin_id": nfl_admin_id
        }
        
        try:
            response = requests.post(f"{FASTAPI_URL}/schedule_game", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    st.success(f"Success: {data.get('message', 'Game scheduled successfully!')}")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")