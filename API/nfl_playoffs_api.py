from fastapi import FastAPI, Query
from get_teams_by_conference_division import get_teams_by_conference_division
from get_teams_in_same_conference_division_as_specified_team import get_teams_in_same_division
from validate_user import validate_user

app = FastAPI()

@app.get("/get_teams_by_conference_division")
def read_teams(conference: str = None, division: str = None):
    try:
        teams = get_teams_by_conference_division(conference, division)
        return teams
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_teams_in_same_conference_division_as_specified_team")
def read_teams_by_team(team_name: str = Query(..., description="Enter Team Name")):
    try:
        teams = get_teams_in_same_division(team_name)
        return teams
    except Exception as e:
        return {"error": str(e)}

@app.post("/validate_user")
def api_validate_user(email: str, password: str):
    return validate_user(email, password)