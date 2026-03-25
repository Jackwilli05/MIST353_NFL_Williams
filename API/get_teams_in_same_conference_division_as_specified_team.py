from get_db_connection import get_db_connection

def get_teams_in_same_division(team_name):
    if not team_name or team_name.strip() == "":
        return {"error": "Team Name is required."}
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("EXEC procGetTeamsInSameConferenceDivisionAsSpecifiedTeam @TeamName = ?", (team_name,))
        
        # Get column names
        columns = [column[0] for column in cursor.description]
        
        # Fetch all rows and convert to list of dictionaries
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        
        cursor.close()
        conn.close()
        
        return result if result else {"message": f"No teams found for {team_name}"}
        
    except Exception as e:
        return {"error": str(e)}