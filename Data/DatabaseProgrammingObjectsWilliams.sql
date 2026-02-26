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
