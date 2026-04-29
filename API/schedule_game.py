rom get_db_connection import get_db_connection

def schedule_game(home_team_id: int, away_team_id: int, game_round: str, game_date: str, game_start_time: str, stadium_id: int, nfl_admin_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        
        cursor.execute("""
            EXEC procScheduleGame 
                @HomeTeamID = %s, 
                @AwayTeamID = %s, 
                @GameRound = %s, 
                @GameDate = %s, 
                @GameStartTime = %s, 
                @StadiumID = %s, 
                @NFLAdminID = %s
        """, (home_team_id, away_team_id, game_round, game_date, game_start_time, stadium_id, nfl_admin_id))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"message": "Game scheduled successfully"}
    except Exception as e:
        return {"error": str(e)}