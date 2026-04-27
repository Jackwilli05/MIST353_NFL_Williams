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

CREATE OR ALTER PROCEDURE procValidateUser
(
    @Email NVARCHAR(100),
    @PasswordHash NVARCHAR(200)
)
AS
BEGIN
    SELECT AppUserID, Firstname + ' ' + Lastname AS Fullname, UserRole
    FROM AppUser
    WHERE Email = @Email 
      AND PasswordHash = CONVERT(VARBINARY(200), @PasswordHash, 1);
END;
GO

-- execute procValidateUser @Email = 'tom.brady@example.com', @PasswordHash = '0x01';

CREATE OR ALTER PROCEDURE procGetTeamsForSpecifiedFan
(
    @Email NVARCHAR(100)
)
AS
BEGIN
    SELECT t.TeamID, t.TeamName, t.TeamCityState, t.TeamColors, cd.Conference, cd.Division
    FROM FanTeam ft
    INNER JOIN AppUser au ON ft.NFLFanID = au.AppUserID
    INNER JOIN Team t ON ft.TeamID = t.TeamID
    INNER JOIN ConferenceDivision cd ON t.ConferenceDivisionID = cd.ConferenceDivisionID
    WHERE au.Email = @Email;
END;
GO

CREATE OR ALTER PROCEDURE procScheduleGame
(
    @HomeTeamID INT,
    @AwayTeamID INT,
    @GameRound NVARCHAR(50),
    @GameDate DATE,
    @GameStartTime TIME,
    @StadiumID INT,
    @NFLAdminID INT -- the logged-in admin who is scheduling the game
)
AS
BEGIN
    -- Store the NFLAdminID in context so that the trigger can access it when inserting into AdminChangesTracker
    DECLARE @context VARBINARY(128) = CAST(@NFLAdminID AS VARBINARY(128));
    SET CONTEXT_INFO @context;

    INSERT INTO Game (HomeTeamID, AwayTeamID, GameRound, GameDate, GameStartTime, StadiumID)
    VALUES (@HomeTeamID, @AwayTeamID, @GameRound, @GameDate, @GameStartTime, @StadiumID);
END;
GO

CREATE OR ALTER TRIGGER trgTrackChangesOnSchedulingGame
ON Game
AFTER INSERT
AS
BEGIN
    DECLARE @NFLAdminID INT;
    DECLARE @GameID INT;
    DECLARE @ChangeType NVARCHAR(50);
    DECLARE @ChangeDescription NVARCHAR(500);
    DECLARE @GameRound NVARCHAR(50);
    DECLARE @GameDate DATE;
    DECLARE @GameStartTime TIME;
    DECLARE @HomeTeamID INT;
    DECLARE @AwayTeamID INT;
    DECLARE @HomeTeamName NVARCHAR(50);
    DECLARE @AwayTeamName NVARCHAR(50);
    DECLARE @StadiumID INT;
    DECLARE @StadiumName NVARCHAR(100);

    -- Get the NFLAdminID from context (set by the stored procedure)
    SET @NFLAdminID = CONVERT(INT, CONVERT(BINARY(4), CONTEXT_INFO()));

    -- Get the GameID of the newly inserted game
    SELECT 
        @GameID = GameID, 
        @GameRound = GameRound, 
        @GameDate = GameDate, 
        @GameStartTime = GameStartTime,
        @HomeTeamID = HomeTeamID, 
        @AwayTeamID = AwayTeamID, 
        @StadiumID = StadiumID
    FROM inserted;

    -- Get names from related tables
    SELECT @HomeTeamName = TeamName FROM Team WHERE TeamID = @HomeTeamID;
    SELECT @AwayTeamName = TeamName FROM Team WHERE TeamID = @AwayTeamID;
    SELECT @StadiumName = StadiumName FROM Stadium WHERE StadiumID = @StadiumID;

    -- Set change type and description
    SET @ChangeType = 'Insert';
    SET @ChangeDescription = 'Scheduled a new game with GameID ' + CAST(@GameID AS NVARCHAR(50)) 
        + ': ' + @HomeTeamName + ' vs ' + @AwayTeamName + ' on ' + CAST(@GameDate AS NVARCHAR(50)) 
        + ' at ' + CAST(@GameStartTime AS NVARCHAR(50)) + ' in stadium ' + @StadiumName 
        + '. Game round: ' + @GameRound;

    -- Insert into AdminChangesTracker
    INSERT INTO AdminChangesTracker (NFLAdminID, GameID, ChangeType, ChangeDescription)
    VALUES (@NFLAdminID, @GameID, @ChangeType, @ChangeDescription);
END;
GO


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



create login APIlogin
with PASSWORD = 'Boris0707!'

Create user APIUser
For LOGIN APIlogin;

Grant execute to APIUser;

Grant select to APIUser;


EXEC procGetTeamsInSameConferenceDivisionAsSpecifiedTeam @TeamName = 'Baltimore Ravens';

UPDATE AppUser 
SET UserRole = 'NFL Fan'
WHERE Email = 'tom.brady@example.com';

