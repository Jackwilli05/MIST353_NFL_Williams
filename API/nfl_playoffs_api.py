from fastapi import FastAPI, Query
from get_teams_by_conference_division import get_teams_by_conference_division
from get_teams_in_same_conference_division_as_specified_team import get_teams_in_same_division

app = FastAPI()

@app.get("/get_teams_by_conference_division")
def read_teams(conference: str = None, division: str = None):
    """Read teams from a conference and division."""
    try:
        teams = get_teams_by_conference_division(conference, division)
        return teams
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_teams_in_same_conference_division_as_specified_team")
def get_teams_in_same_conference_division_api(team_name: str = Query(...)):
    """Get teams in same conference/division as specified team."""
    try:
        return get_teams_in_same_division(team_name)
    except Exception as e:
        return {"error": str(e)}