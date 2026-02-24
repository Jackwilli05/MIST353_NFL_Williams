-- 3 queries 
-- 1 each for conferencedivision and team tables, and 1 join query 



USE MIST353_NFL_RDB_Williams;
GO

-- Query 1: ConferenceDivision table
SELECT * FROM ConferenceDivision;
GO

-- Query 2: Team table
SELECT * FROM Team;
GO

-- Query 3: Join query 
SELECT 
    t.TeamName,
    t.TeamCityState,
    t.TeamColors,
    cd.Conference,
    cd.Division
FROM Team t
    JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
ORDER BY cd.Conference, cd.Division, t.TeamName;
GO