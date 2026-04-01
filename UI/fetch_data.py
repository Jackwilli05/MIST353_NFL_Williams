import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

def fetch_data(endpoint: str, input_params: dict, method: str = "GET"):
    try:
        response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=input_params)
        
        if response.status_code == 200:
            data = response.json()
            # If data is a list, return it directly
            if isinstance(data, list):
                return data
            # If data is a dict with a 'data' key, return that
            if isinstance(data, dict) and "data" in data:
                return data["data"]
            # Otherwise return the data as is
            return data
        else:
            st.error(f"Error: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []