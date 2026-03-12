def get_teams_by_conference_division(conference, division):
    from get_db_connection import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC procTeamsByConferenceDivision @ConferenceName = ?, @DivisionName = ?", (conference, division))
    teams = cursor.fetchall()
    cursor.close()
    conn.close()
    return teams