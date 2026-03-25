-- 3 queries 
-- 1 each for conferencedivision and team tables, and 1 join query 



USE MIST353_NFL_RDB_Williams;
GO


-- Query 1: 
SELECT * FROM ConferenceDivision;
GO

-- Query 2: 
SELECT * FROM Team;
GO

-- Query 3: 
/*
create or alter procedure procTeamsByConferenceDivision
(
    @ConferenceName NVARCHAR(50) = null,
    @DivisionName NVARCHAR(50) = null
)
AS
begin
    select TeamName, TeamColors, Conference, Division
    from Team T inner join ConferenceDivision C
    on T.ConferenceDivisionID = C.ConferenceDivisionID
    where Conference = IsNull(@ConferenceName, Conference)
    and Division = IsNull(@DivisionName, Division)
end
go
*/


/*
CREATE OR ALTER PROCEDURE procGetTeamsInSameConferenceDivisionAsSpecifiedTeam
(
    @TeamName NVARCHAR(100)
)
AS
BEGIN
    SELECT t.TeamName, t.TeamColors, cd.Conference, cd.Division
    FROM Team t
    INNER JOIN ConferenceDivision cd
        ON t.ConferenceDivisionID = cd.ConferenceDivisionID
    WHERE cd.ConferenceDivisionID = (
        SELECT ConferenceDivisionID
        FROM Team
        WHERE TeamName = @TeamName
    )
    AND t.TeamName != @TeamName
    ORDER BY t.TeamName;
END;
*/

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';

-- Check ConferenceDivision table
SELECT COUNT(*) AS ConferenceDivisionCount FROM ConferenceDivision;

-- Check Team table
SELECT COUNT(*) AS TeamCount FROM Team;

SELECT name 
FROM sys.databases 
WHERE name LIKE '%RDB%';

SELECT TeamName FROM Team WHERE TeamName LIKE '%Ravens%';

-- See all conferences and divisions
SELECT * FROM ConferenceDivision;

-- See first 10 teams
SELECT TOP 10 TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID 
FROM Team 
ORDER BY TeamID;


/*
create login APIlogin
with PASSWORD = 'Boris0707!'

Create user APIUser
For LOGIN APIlogin;

Grant execute to APIUser;

Grant select to APIUser;


EXEC procGetTeamsInSameConferenceDivisionAsSpecifiedTeam @TeamName = 'Baltimore Ravens';

