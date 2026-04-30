from get_db_connection import get_db_connection

def get_all_changes_made_by_specified_admin(
        nfl_admin_id: int
    ):
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.callproc("procGetAllChangesMadeBySpecifiedAdmin", (nfl_admin_id,))
    rows = cursor.fetchall()
    conn.close()

    #Convert pymssql.Row objects to dicts
    results = [
        {
            "ChangeType": row["ChangeType"],
            "ChangeDescription": row["ChangeDescription"],
            "ChangeDateTime": row["ChangeDateTime"],
            "GameDate": row["GameDate"],
            "GameStartTime": row["GameStartTime"],
            "GameRound": row["GameRound"],
            "HomeTeam": row["HomeTeam"],
            "AwayTeam": row["AwayTeam"]
        }
        for row in rows
    ]

    return {"data": results}
