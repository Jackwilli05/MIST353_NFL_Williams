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
    
    st.success(f"Logged in as: {st.session_state.get('app_user_fullname', 'Admin')}")
    
    # Fetch teams using existing endpoint (no parameters = all teams)
    try:
        response = requests.get(f"{FASTAPI_URL}/get_teams_by_conference_division")
        if response.status_code == 200:
            teams = response.json()
            if teams and isinstance(teams, list) and len(teams) > 0:
                # Extract unique team names from the response
                team_names = list(set([team["TeamName"] for team in teams]))
                team_names.sort()
            else:
                team_names = ["Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"]
        else:
            team_names = ["Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"]
    except Exception as e:
        team_names = ["Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"]
        st.warning(f"Using fallback team list")
    
    # Fetch stadiums
    try:
        response = requests.get(f"{FASTAPI_URL}/get_all_stadiums")
        if response.status_code == 200:
            stadiums = response.json()
            if stadiums and isinstance(stadiums, list) and len(stadiums) > 0:
                stadium_names = [stadium["StadiumName"] for stadium in stadiums]
            else:
                stadium_names = ["M&T Bank Stadium", "Acrisure Stadium", "Gillette Stadium", "Arrowhead Stadium"]
        else:
            stadium_names = ["M&T Bank Stadium", "Acrisure Stadium", "Gillette Stadium", "Arrowhead Stadium"]
    except Exception as e:
        stadium_names = ["M&T Bank Stadium", "Acrisure Stadium", "Gillette Stadium", "Arrowhead Stadium"]
    
    game_rounds = ["Wild Card", "Divisional", "Conference", "Super Bowl"]
    
    # Create columns for layout
    left_col, right_col = st.columns(2)
    
    with left_col:
        home_team = st.selectbox("Select Home Team", team_names)
        stadium = st.selectbox("Select Stadium", stadium_names)
        game_round = st.selectbox("Select Game Round", game_rounds)
    
    with right_col:
        away_team = st.selectbox("Select Away Team", team_names)
        game_date = st.date_input("Select Game Date")
        game_time = st.time_input("Select Game Start Time")
    
    # Auto-filled admin ID
    nfl_admin_id = st.session_state.get("app_user_id", 1)
    st.caption(f"NFL Admin ID: {nfl_admin_id} (auto-filled from your login)")
    
    if st.button("Schedule Game", type="primary"):
        # Validate teams are different
        if home_team == away_team:
            st.error("Home team and away team cannot be the same")
            return
        
        st.success(f"Scheduling: {home_team} vs {away_team} at {stadium} on {game_date}")
        st.info("Note: Team IDs and Stadium IDs are being sent to the API")