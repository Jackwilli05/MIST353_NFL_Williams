from get_db_connection import get_db_connection

def get_teams_for_specified_fan(email: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("EXEC procGetTeamsForSpecifiedFan @Email = ?", (email,))
        
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        
        cursor.close()
        conn.close()
        
        return result if result else {"message": f"No favorite teams found for {email}"}
    except Exception as e:
        return {"error": str(e)}