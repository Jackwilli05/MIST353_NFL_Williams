import streamlit as st
import requests
from fetch_data import fetch_data

FASTAPI_URL = "https://mist353-api-williams.azurewebsites.net"

def schedule_game_ui():
    st.header("Schedule a New Game")
    
    # Check if user is logged in as NFL Admin
    if not st.session_state.get("is_authenticated", False):
        st.error("Please login to schedule games")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
        return
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    # Fetch teams for dropdown
    teams = fetch_data("get_teams_by_conference_division", {})
    if teams and isinstance(teams, list) and len(teams) > 0:
        team_names = [team["TeamName"] for team in teams]
        team_dict = {team["TeamName"]: team["TeamID"] for team in teams}
    else:
        team_names = []
        team_dict = {}
        st.warning("Could not load teams. Please check your connection.")
    
    # Fetch stadiums for dropdown
    stadiums = fetch_data("get_all_stadiums", {})
    if stadiums and isinstance(stadiums, list) and len(stadiums) > 0:
        stadium_names = [stadium["StadiumName"] for stadium in stadiums]
        stadium_dict = {stadium["StadiumName"]: stadium["StadiumID"] for stadium in stadiums}
    else:
        stadium_names = []
        stadium_dict = {}
        st.warning("Could not load stadiums. Please check your connection.")
    
    # Game rounds
    game_rounds = ["Wild Card", "Divisional", "Conference", "Super Bowl"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        if team_names:
            home_team = st.selectbox("Select Home Team", team_names)
            home_team_id = team_dict.get(home_team, 0)
        else:
            home_team_id = st.number_input("Home Team ID", min_value=1, max_value=32, step=1)
        
        if stadium_names:
            stadium = st.selectbox("Select Stadium", stadium_names)
            stadium_id = stadium_dict.get(stadium, 0)
        else:
            stadium_id = st.number_input("Stadium ID", min_value=1, step=1)
    
    with col2:
        if team_names:
            away_team = st.selectbox("Select Away Team", team_names)
            away_team_id = team_dict.get(away_team, 0)
        else:
            away_team_id = st.number_input("Away Team ID", min_value=1, max_value=32, step=1)
    
    game_round = st.selectbox("Select Game Round", game_rounds)
    game_date = st.date_input("Select Game Date")
    game_time = st.time_input("Select Game Start Time")
    
    nfl_admin_id = st.session_state.get("app_user_id", 1)
    st.info(f"NFL Admin ID: {nfl_admin_id} (auto-filled from your login)")
    
    if st.button("Schedule Game", type="primary"):
        # Check if home and away teams are the same
        if home_team_id == away_team_id:
            st.error("Home team and away team cannot be the same")
            return
        
        if home_team_id == 0 or away_team_id == 0 or stadium_id == 0:
            st.error("Please select valid teams and stadium")
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
                    st.error(f"Database Error: {data['error']}")
                else:
                    st.success("Game scheduled successfully!")
                    st.balloons()
            else:
                st.error(f"API Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")