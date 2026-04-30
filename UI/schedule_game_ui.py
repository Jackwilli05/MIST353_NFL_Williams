import streamlit as st
from fetch_data import post_data

def schedule_game_ui():
    st.header("Schedule a New Game")
    
    if not st.session_state.get("is_authenticated", False):
        st.warning("Please login as NFL Admin to schedule games")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
        return
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    home_team_id = st.number_input("Home Team ID", min_value=1, max_value=32, step=1)
    away_team_id = st.number_input("Away Team ID", min_value=1, max_value=32, step=1)
    game_round = st.selectbox("Game Round", ["Wild Card", "Divisional", "Conference", "Super Bowl"])
    game_date = st.date_input("Game Date")
    game_start_time = st.time_input("Game Start Time")
    stadium_id = st.number_input("Stadium ID", min_value=1, step=1)
    nfl_admin_id = st.number_input("NFL Admin ID", min_value=1, step=1, value=st.session_state.get("app_user_id", 1))
    
    if st.button("Schedule Game"):
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
        
        result = post_data("schedule_game", payload)
        
        if result and "error" not in result:
            st.success("Game scheduled successfully!")
        else:
            st.error(f"Failed: {result.get('error', 'Unknown error')}")