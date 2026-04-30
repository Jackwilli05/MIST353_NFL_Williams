from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from get_teams_by_conference_division import get_teams_by_conference_division
from get_teams_in_same_conference_division_as_specified_team import get_teams_in_same_division
from get_teams_for_specified_fan import get_teams_for_specified_fan
from validate_user import validate_user
from schedule_game import schedule_game

app = FastAPI(title="NFL Playoffs API")

# Enable CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "NFL Playoffs API"}

@app.post("/validate_user")
def api_validate_user(email: str, password: str):
    return validate_user(email, password)

@app.get("/get_teams_by_conference_division")
def read_teams(conference: str = None, division: str = None):
    return get_teams_by_conference_division(conference, division)

@app.get("/get_teams_in_same_conference_division_as_specified_team")
def read_teams_by_team(team_name: str = Query(..., description="Enter Team Name")):
    return get_teams_in_same_division(team_name)

@app.get("/get_teams_for_specified_fan")
def read_fan_teams(email: str = Query(..., description="Enter Fan's Email")):
    return get_teams_for_specified_fan(email)

@app.post("/schedule_game")
def api_schedule_game(
    home_team_id: int,
    away_team_id: int,
    game_round: str,
    game_date: str,
    game_time: str,
    stadium_id: int,
    nfl_admin_id: int
):
    return schedule_game(
        home_team_id,
        away_team_id,
        game_round,
        game_date,
        game_time,
        stadium_id,
        nfl_admin_id
    )