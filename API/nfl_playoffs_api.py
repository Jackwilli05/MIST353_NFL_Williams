from fastapi import FastAPI, Query
from get_teams_by_conference_division import get_teams_by_conference_division
from get_teams_in_same_conference_division_as_specified_team import get_teams_in_same_division
from get_teams_for_specified_fan import get_teams_for_specified_fan
from validate_user import validate_user

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NFL Playoffs API"}

@app.get("/get_teams_by_conference_division")
def read_teams(conference: str = None, division: str = None):
    return get_teams_by_conference_division(conference, division)

@app.get("/get_teams_in_same_conference_division_as_specified_team")
def read_teams_by_team(team_name: str = Query(..., description="Enter Team Name")):
    return get_teams_in_same_division(team_name)

@app.get("/get_teams_for_specified_fan")
def read_fan_teams(email: str = Query(..., description="Enter Fan's Email")):
    return get_teams_for_specified_fan(email)

@app.post("/validate_user")
def api_validate_user(email: str, password: str):
    return validate_user(email, password)