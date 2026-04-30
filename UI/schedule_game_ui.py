import streamlit as st
import requests

FASTAPI_URL = "https://mist353-api-williams.azurewebsites.net"

def schedule_game_ui():
    st.header("Schedule a New Game")
    
    if not st.session_state.get("is_authenticated", False):
        st.warning("Please login as NFL Admin to schedule games")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
        return
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        home_team_id = st.number_input("home_team_id", min_value=1, max_value=32, step=1)
        game_round = st.selectbox("game_round", ["Wild Card", "Divisional", "Conference", "Super Bowl"])
        game_date = st.date_input("game_date")
        stadium_id = st.number_input("stadium_id", min_value=1, step=1)
    
    with col2:
        away_team_id = st.number_input("away_team_id", min_value=1, max_value=32, step=1)
        game_time = st.time_input("game_time")
        nfl_admin_id = st.number_input("nfl_admin_id", min_value=1, step=1, value=st.session_state.get("app_user_id", 1))
    
    if st.button("Schedule Game"):
        if home_team_id == away_team_id:
            st.error("Home team and away team cannot be the same")
            return
        
        # Send as query parameters (params=) - matching Swagger parameter names
        params = {
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_round": game_round,
            "game_date": str(game_date),
            "game_time": str(game_time),
            "stadium_id": stadium_id,
            "nfl_admin_id": nfl_admin_id
        }
        
        try:
            response = requests.post(f"{FASTAPI_URL}/schedule_game", params=params)
            
            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    st.success("Game scheduled successfully!")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")