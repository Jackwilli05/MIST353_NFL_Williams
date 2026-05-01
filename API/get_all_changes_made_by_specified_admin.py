from get_db_connection import get_db_connection

def get_all_changes_made_by_specified_admin(nfl_admin_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        cursor.execute("EXEC procGetAllChangesMadeBySpecifiedAdmin @NFLAdminID = %s", (nfl_admin_id,))
        
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result if result else {"message": f"No changes found for admin {nfl_admin_id}"}
    except Exception as e:
        return {"error": str(e)}