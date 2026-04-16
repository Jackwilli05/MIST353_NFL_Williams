import streamlit as st
from get_teams_by_conference_division_ui import get_teams_by_conference_division_ui
from get_teams_in_same_conference_division_as_specified_team_ui import get_teams_in_same_conference_division_as_specified_team_ui
from validate_user_ui import validate_user_ui
from get_teams_for_specified_fan_ui import get_teams_for_specified_fan_ui

st.title("NFL Playoffs API")

page = st.sidebar.selectbox("Choose", [
    "By Conference/Division",
    "By Team",
    "Validate User",
    "Fan's Favorite Teams"
])

if page == "By Conference/Division":
    get_teams_by_conference_division_ui()
elif page == "By Team":
    get_teams_in_same_conference_division_as_specified_team_ui()
elif page == "Validate User":
    validate_user_ui()
else:
    get_teams_for_specified_fan_ui()