from get_db_connection import get_db_connection

def get_teams_by_conference_division(conference=None, division=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("EXEC procTeamsByConferenceDivision @ConferenceName = ?, @DivisionName = ?",
                       (conference, division))
        
        # Get column names
        columns = [column[0] for column in cursor.description]
        
        # Fetch all rows and convert to list of dictionaries
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        
        cursor.close()
        conn.close()
        return result
        
    except Exception as e:
        return {"error": str(e)}