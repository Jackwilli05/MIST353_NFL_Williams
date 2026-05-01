import streamlit as st
import requests

FASTAPI_URL = "https://mist353-api-williams.azurewebsites.net"

def schedule_game_ui():
    st.subheader("Schedule a New Game")
    
    if not st.session_state.get("is_authenticated", False):
        st.warning("Please login as NFL Admin to schedule games")
        return
    
    if st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
        return
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    # Fetch teams
    try:
        response = requests.get(f"{FASTAPI_URL}/get_teams_by_conference_division")
        if response.status_code == 200:
            teams = response.json()
            team_names = [team["TeamName"] for team in teams]
            team_ids = {team["TeamName"]: team["TeamID"] for team in teams}
        else:
            st.error("Could not load teams")
            return
    except Exception as e:
        st.error(f"Error loading teams: {e}")
        return
    
    # Fetch stadiums
    try:
        response = requests.get(f"{FASTAPI_URL}/get_all_stadiums")
        if response.status_code == 200:
            stadiums = response.json()
            stadium_names = [stadium["StadiumName"] for stadium in stadiums]
            stadium_ids = {stadium["StadiumName"]: stadium["StadiumID"] for stadium in stadiums}
        else:
            st.error("Could not load stadiums")
            return
    except Exception as e:
        st.error(f"Error loading stadiums: {e}")
        return
    
    game_rounds = ["Wild Card", "Divisional", "Conference", "Super Bowl"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        home_team = st.selectbox("Select Home Team", team_names)
        stadium = st.selectbox("Select Stadium", stadium_names)
        game_round = st.selectbox("Select Game Round", game_rounds)
    
    with col2:
        away_team = st.selectbox("Select Away Team", team_names)
        game_date = st.date_input("Select Game Date")
        game_time = st.time_input("Select Game Start Time")
    
    nfl_admin_id = st.session_state.get("app_user_id", 1)
    st.caption(f"NFL Admin ID: {nfl_admin_id}")
    
    if st.button("Schedule Game"):
        if home_team == away_team:
            st.error("Home team and away team cannot be the same")
            return
        
        home_team_id = team_ids.get(home_team)
        away_team_id = team_ids.get(away_team)
        stadium_id = stadium_ids.get(stadium)
        
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
                    st.success("Game scheduled successfully")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Connection error: {e}")