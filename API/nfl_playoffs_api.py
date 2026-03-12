from fastapi import FastAPI, Query
import pandas as pd
from get_teams_from_same_cd_fn import get_teams_from_same_cd

app = FastAPI(title="NFL Playoffs API")

@app.get("/")
def root():
    return {
        "message": "NFL Playoffs API",
        "endpoints": [
            "/get_teams_from_specified_conference_division/",
            "/docs"
        ]
    }

@app.get("/get_teams_from_specified_conference_division/")
def get_teams_from_specified_conference_division(
    team_name: str = Query(..., description="Enter Team Name:")
):
    """
    Get all teams in the same conference/division as the specified team
    """
    result = get_teams_from_same_cd(team_name)
    
    if isinstance(result, pd.DataFrame):
        return result.to_dict(orient='records')
    else:
        return result