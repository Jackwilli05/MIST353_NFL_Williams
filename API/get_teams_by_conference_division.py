from get_db_connection import get_db_connection

def get_teams_by_conference_division(conference=None, division=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        cursor.execute(
            "EXEC procTeamsByConferenceDivision @ConferenceName = %s, @DivisionName = %s",
            (conference, division)
        )
        
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result if result else []
    except Exception as e:
        return {"error": str(e)}