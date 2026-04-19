from get_db_connection import get_db_connection

def validate_user(email: str, password: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        cursor.execute(
            "EXEC procValidateUser @Email = %s, @PasswordHash = %s",
            (email, password)
        )
        
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result if result else {"message": "Invalid email or password"}
    except Exception as e:
        return {"error": str(e)}