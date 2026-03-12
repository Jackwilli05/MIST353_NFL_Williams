import pandas as pd
from get_db_connection import get_db_connection

def get_teams_from_same_cd(team_name):
    """
    Get all teams in the same conference/division as the specified team
    """
    if not team_name or team_name.strip() == "":
        return {"error": "Team Name is required."}
    
    team_name = team_name.strip()
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Call your stored procedure
        cursor.execute("EXEC procGetOtherTeamsByTeam @TeamName = ?", (team_name,))
        
        # Get column names
        columns = [column[0] for column in cursor.description]
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Convert to list of dictionaries (fixes the shape error)
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        
        cursor.close()
        conn.close()
        
        if result:
            return result
        else:
            return {"message": f"No teams found for {team_name}"}
            
    except Exception as e:
        return {"error": str(e)}