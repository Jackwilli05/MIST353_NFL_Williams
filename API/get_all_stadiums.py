from get_db_connection import get_db_connection

def get_all_stadiums():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT StadiumID, StadiumName, StadiumCityState, Capacity FROM Stadium ORDER BY StadiumName")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return {"error": str(e)}
