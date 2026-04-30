import streamlit as st
from fetch_data import fetch_data

def get_all_changes_made_by_specified_admin_ui():

    nfl_admin_name = st.session_state.app_user_fullname
    st.header(f"Changes made by {nfl_admin_name}")

    input_parameters = {}
    nfl_admin_id = st.text_input("NFL Admin ID", value=st.session_state.app_user_id, disabled=True)
    input_parameters["nfl_admin_id"] = nfl_admin_id

    df = fetch_data("get_all_changes_made_by_specified_admin/", input_parameters)

    if df is not None and not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No changes found for the specified admin.")