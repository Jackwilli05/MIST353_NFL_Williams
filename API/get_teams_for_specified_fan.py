from get_db_connection import get_db_connection

def get_teams_for_specified_fan(email: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        # Professor's required syntax for stored procedure
        cursor.execute("exec procGetTeamsForSpecifiedFan %s", (email,))
        
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result if result else {"message": f"No favorite teams found for {email}"}
    except Exception as e:
        return {"error": str(e)}