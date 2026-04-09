import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

def fetch_data(endpoint: str, input_params: dict, method: str = "GET"):
    try:
        if method == "GET":
            response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=input_params)
        else:
            response = requests.post(f"{FASTAPI_URL}/{endpoint}", params=input_params)
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and "data" in data:
                return data["data"]
            return data
        else:
            st.error(f"Error: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []