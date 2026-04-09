from get_db_connection import get_db_connection

def validate_user(email: str, password: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("EXEC procValidateUser @Email = ?, @PasswordHash = ?", (email, password))
        
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        
        cursor.close()
        conn.close()
        
        return result if result else {"message": "Invalid email or password"}
    except Exception as e:
        return {"error": str(e)}