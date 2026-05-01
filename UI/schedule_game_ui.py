import streamlit as st
import requests
from fetch_data import fetch_data

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
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    # Fetch teams for dropdown with error handling
    try:
        teams = fetch_data("get_teams_by_conference_division", {})
        if teams and isinstance(teams, list) and len(teams) > 0:
            team_options = {team["TeamName"]: team["TeamID"] for team in teams}
        else:
            team_options = {}
            st.warning("Could not load teams. Using manual ID entry.")
    except Exception as e:
        team_options = {}
        st.warning(f"Could not load teams: {e}. Using manual ID entry.")
    
    # Fetch stadiums for dropdown with error handling
    try:
        stadiums = fetch_data("get_all_stadiums", {})
        if stadiums and isinstance(stadiums, list) and len(stadiums) > 0:
            stadium_options = {stadium["StadiumName"]: stadium["StadiumID"] for stadium in stadiums}
        else:
            stadium_options = {}
            st.warning("Could not load stadiums. Using manual ID entry.")
    except Exception as e:
        stadium_options = {}
        st.warning(f"Could not load stadiums: {e}. Using manual ID entry.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if team_options:
            home_team_name = st.selectbox("Home Team", list(team_options.keys()))
            home_team_id = team_options[home_team_name]
        else:
            home_team_id = st.number_input("Home Team ID", min_value=1, max_value=32, step=1)
        
        game_round = st.selectbox("Game Round", ["Wild Card", "Divisional", "Conference", "Super Bowl"])
        game_date = st.date_input("Game Date")
        
        if stadium_options:
            stadium_name = st.selectbox("Stadium", list(stadium_options.keys()))
            stadium_id = stadium_options[stadium_name]
        else:
            stadium_id = st.number_input("Stadium ID", min_value=1, step=1)
    
    with col2:
        if team_options:
            away_team_name = st.selectbox("Away Team", list(team_options.keys()))
            away_team_id = team_options[away_team_name]
        else:
            away_team_id = st.number_input("Away Team ID", min_value=1, max_value=32, step=1)
        
        game_time = st.time_input("Game Start Time")
        nfl_admin_id = st.session_state.get("app_user_id", 1)
        st.info(f"NFL Admin ID: {nfl_admin_id} (auto-filled)")
    
    if st.button("Schedule Game", type="primary"):
        # Check if home and away teams are the same
        if home_team_id == away_team_id:
            st.error("Home team and away team cannot be the same")
            return
        
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
                    st.balloons()
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")
