from get_db_connection import get_db_connection

def get_teams_by_conference_division(conference=None, division=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        if conference and division:
            cursor.execute("""
                SELECT t.TeamID, t.TeamName, t.TeamColors, cd.Conference, cd.Division
                FROM Team t
                INNER JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
                WHERE cd.Conference = %s AND cd.Division = %s
                ORDER BY t.TeamName
            """, (conference, division))
        elif conference:
            cursor.execute("""
                SELECT t.TeamID, t.TeamName, t.TeamColors, cd.Conference, cd.Division
                FROM Team t
                INNER JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
                WHERE cd.Conference = %s
                ORDER BY t.TeamName
            """, (conference,))
        elif division:
            cursor.execute("""
                SELECT t.TeamID, t.TeamName, t.TeamColors, cd.Conference, cd.Division
                FROM Team t
                INNER JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
                WHERE cd.Division = %s
                ORDER BY t.TeamName
            """, (division,))
        else:
            cursor.execute("""
                SELECT t.TeamID, t.TeamName, t.TeamColors, cd.Conference, cd.Division
                FROM Team t
                INNER JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
                ORDER BY t.TeamName
            """)
        
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return {"error": str(e)}