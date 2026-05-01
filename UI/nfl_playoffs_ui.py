import streamlit as st
from get_teams_by_conference_division_ui import get_teams_by_conference_division_ui
from get_teams_in_same_conference_division_as_specified_team_ui import get_teams_in_same_conference_division_as_specified_team_ui
from validate_user_ui import validate_user_ui
from get_teams_for_specified_fan_ui import get_teams_for_specified_fan_ui
from get_teams_with_logos_for_specified_fan_ui import get_teams_with_logos_for_specified_fan_ui
from schedule_game_ui import schedule_game_ui
from get_all_changes_made_by_specified_admin_ui import get_all_changes_made_by_specified_admin_ui

st.set_page_config(page_title="NFL Playoffs App", layout="wide")

st.title("NFL Playoffs App")

# Show welcome message based on login status
if st.session_state.get("is_authenticated", False):
    st.markdown(f"### Welcome to the NFL Playoffs App, **{st.session_state.app_user_fullname}**!")
    st.caption("Use the sidebar to navigate through different features.")
else:
    st.markdown("### Welcome to the NFL Playoffs App!")
    st.caption("Please login using 'Validate User' to access all features.")

st.sidebar.title("Navigation")

# Dropdown menu based on user role
if st.session_state.get("is_authenticated", False):
    if st.session_state.get("user_role") == "NFLAdmin":
        page = st.sidebar.selectbox("Choose a feature", [
            "Validate User",
            "Get Teams by Conference/Division",
            "Get Teams in Same Division as Team",
            "Get Favorite Teams for Fan",
            "Get Favorite Teams with Logos",
            "Schedule Game",
            "View Admin Change History"
        ])
    else:
        page = st.sidebar.selectbox("Choose a feature", [
            "Validate User",
            "Get Teams by Conference/Division",
            "Get Teams in Same Division as Team",
            "Get Favorite Teams for Fan",
            "Get Favorite Teams with Logos"
        ])
else:
    page = st.sidebar.selectbox("Choose a feature", [
        "Validate User",
        "Get Teams by Conference/Division",
        "Get Teams in Same Division as Team",
        "Get Favorite Teams for Fan"
    ])

# Page routing
if page == "Validate User":
    validate_user_ui()
elif page == "Get Teams by Conference/Division":
    get_teams_by_conference_division_ui()
elif page == "Get Teams in Same Division as Team":
    get_teams_in_same_conference_division_as_specified_team_ui()
elif page == "Get Favorite Teams for Fan":
    get_teams_for_specified_fan_ui()
elif page == "Get Favorite Teams with Logos":
    get_teams_with_logos_for_specified_fan_ui()
elif page == "Schedule Game":
    schedule_game_ui()
elif page == "View Admin Change History":
    get_all_changes_made_by_specified_admin_ui()

st.sidebar.markdown("---")
if st.session_state.get("is_authenticated", False):
    st.sidebar.info(f"Logged in as: **{st.session_state.app_user_fullname}**\nRole: {st.session_state.user_role}")
else:
    st.sidebar.info("Please login using 'Validate User'")