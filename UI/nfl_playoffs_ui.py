import streamlit as st
from get_teams_by_conference_division_ui import get_teams_by_conference_division_ui
from get_teams_in_same_conference_division_as_specified_team_ui import get_teams_in_same_conference_division_as_specified_team_ui
from validate_user_ui import validate_user_ui
from get_teams_for_specified_fan_ui import get_teams_for_specified_fan_ui

st.set_page_config(page_title="NFL Playoffs API", layout="wide")

st.title("NFL Playoffs App")

# Show welcome message if logged in
if st.session_state.get("is_authenticated", False):
    st.markdown(f"### Welcome to the NFL Playoffs App, **{st.session_state.app_user_fullname}**!")
    st.caption("Use the sidebar to navigate through different features and explore information about NFL teams, players, and playoff matchups.")
else:
    st.markdown("### Welcome to the NFL Playoffs App!")
    st.caption("Use the sidebar to navigate through different features and explore information about NFL teams, players, and playoff matchups.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a feature", [
    "Get Teams by Conference/Division",
    "Get Teams in Same Division as Team",
    "Validate User",
    "Get Favorite Teams for Fan"
])

if page == "Get Teams by Conference/Division":
    get_teams_by_conference_division_ui()
elif page == "Get Teams in Same Division as Team":
    get_teams_in_same_conference_division_as_specified_team_ui()
elif page == "Validate User":
    validate_user_ui()
else:
    get_teams_for_specified_fan_ui()

st.sidebar.markdown("---")
if st.session_state.get("is_authenticated", False):
    st.sidebar.info(f"Logged in as: **{st.session_state.app_user_fullname}**")
else:
    st.sidebar.info("Please login using 'Validate User'")