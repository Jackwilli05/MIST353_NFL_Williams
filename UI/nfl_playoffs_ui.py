import streamlit as st
from get_teams_by_conference_division_ui import get_teams_by_conference_division_ui
from get_teams_in_same_conference_division_as_specified_team_ui import get_teams_in_same_conference_division_as_specified_team_ui


st.title("NFL Playoffs API")

page = st.sidebar.selectbox("Choose", ["By Conference/Division", "By Team"])

if page == "By Conference/Division":
    get_teams_by_conference_division_ui()
else:
    get_teams_in_same_conference_division_as_specified_team_ui()