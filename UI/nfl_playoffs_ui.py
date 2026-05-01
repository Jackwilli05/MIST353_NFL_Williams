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

# Show all options in dropdown for everyone
page = st.sidebar.selectbox("Choose a feature", [
    "Validate User",
    "Get Teams by Conference/Division",
    "Get Teams in Same Division as Team",
    "Get Favorite Teams for Fan",
    "Get Favorite Teams with Logos",
    "Schedule Game",
    "View Admin Change History"
])

# Page routing with login checks for restricted features
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
    # Check if logged in as NFL Admin
    if not st.session_state.get("is_authenticated", False):
        st.error("Please login to schedule games")
    elif st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can schedule games")
    else:
        schedule_game_ui()
elif page == "View Admin Change History":
    # Check if logged in as NFL Admin
    if not st.session_state.get("is_authenticated", False):
        st.error("Please login to view change history")
    elif st.session_state.get("user_role") != "NFLAdmin":
        st.error("Only NFL Admins can view change history")
    else:
        get_all_changes_made_by_specified_admin_ui()

st.sidebar.markdown("---")
if st.session_state.get("is_authenticated", False):
    st.sidebar.info(f"Logged in as: **{st.session_state.app_user_fullname}**\nRole: {st.session_state.user_role}")
else:
    st.sidebar.info("Please login using 'Validate User'")