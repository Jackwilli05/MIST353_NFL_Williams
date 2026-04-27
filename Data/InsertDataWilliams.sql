-- ============================================
-- INSERT DATA
-- ============================================

-- STEP 1: ConferenceDivision
INSERT INTO ConferenceDivision (Conference, Division) VALUES
('AFC', 'North'), ('AFC', 'South'), ('AFC', 'East'), ('AFC', 'West'),
('NFC', 'North'), ('NFC', 'South'), ('NFC', 'East'), ('NFC', 'West');
GO

-- STEP 2: Team (32 NFL Teams)
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
-- AFC North (1)
('Baltimore Ravens', 'Baltimore, MD', 'Purple, Black, Gold', 1),
('Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange, White', 1),
('Cleveland Browns', 'Cleveland, OH', 'Brown, Orange, White', 1),
('Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Gold', 1),
-- AFC South (2)
('Houston Texans', 'Houston, TX', 'Deep Steel Blue, Battle Red', 2),
('Indianapolis Colts', 'Indianapolis, IN', 'Royal Blue, White', 2),
('Jacksonville Jaguars', 'Jacksonville, FL', 'Teal, Black, Gold', 2),
('Tennessee Titans', 'Nashville, TN', 'Navy Blue, Titans Blue', 2),
-- AFC East (3)
('Buffalo Bills', 'Buffalo, NY', 'Royal Blue, Red, White', 3),
('Miami Dolphins', 'Miami Gardens, FL', 'Aqua, Orange, White', 3),
('New England Patriots', 'Foxborough, MA', 'Navy Blue, Red, Silver', 3),
('New York Jets', 'East Rutherford, NJ', 'Gotham Green, White', 3),
-- AFC West (4)
('Denver Broncos', 'Denver, CO', 'Orange, Navy Blue', 4),
('Kansas City Chiefs', 'Kansas City, MO', 'Red, Gold', 4),
('Las Vegas Raiders', 'Las Vegas, NV', 'Silver, Black', 4),
('Los Angeles Chargers', 'Inglewood, CA', 'Powder Blue, Gold', 4),
-- NFC North (5)
('Chicago Bears', 'Chicago, IL', 'Navy Blue, Orange', 5),
('Detroit Lions', 'Detroit, MI', 'Honolulu Blue, Silver', 5),
('Green Bay Packers', 'Green Bay, WI', 'Dark Green, Gold', 5),
('Minnesota Vikings', 'Minneapolis, MN', 'Purple, Gold', 5),
-- NFC South (6)
('Atlanta Falcons', 'Atlanta, GA', 'Red, Black, Silver', 6),
('Carolina Panthers', 'Charlotte, NC', 'Black, Process Blue', 6),
('New Orleans Saints', 'New Orleans, LA', 'Old Gold, Black', 6),
('Tampa Bay Buccaneers', 'Tampa, FL', 'Red, Pewter', 6),
-- NFC East (7)
('Dallas Cowboys', 'Arlington, TX', 'Navy Blue, Silver', 7),
('New York Giants', 'East Rutherford, NJ', 'Royal Blue, Red', 7),
('Philadelphia Eagles', 'Philadelphia, PA', 'Midnight Green, Silver', 7),
('Washington Commanders', 'Landover, MD', 'Burgundy, Gold', 7),
-- NFC West (8)
('Arizona Cardinals', 'Glendale, AZ', 'Cardinal Red, White', 8),
('Los Angeles Rams', 'Inglewood, CA', 'Royal Blue, Yellow', 8),
('San Francisco 49ers', 'Santa Clara, CA', 'Scarlet, Gold', 8),
('Seattle Seahawks', 'Seattle, WA', 'College Navy, Action Green', 8);
GO

-- STEP 3: AppUser
INSERT INTO AppUser (Firstname, Lastname, Email, PasswordHash, UserRole) VALUES
('Tom', 'Brady', 'tom.brady@example.com', 0x01, 'NFLFan'),
('Aaron', 'Rodgers', 'aaron.rodgers@example.com', 0x01, 'NFLFan'),
('Drew', 'Brees', 'drew.brees@example.com', 0x01, 'NFLFan'),
('Patrick', 'Mahomes', 'patrick.mahomes@example.com', 0x01, 'NFLFan'),
('Bill', 'Belichick', 'bill.belichick@example.com', 0x01, 'NFLAdmin'),
('Sean', 'McVay', 'sean.mcvay@example.com', 0x01, 'NFLAdmin'),
('Mike', 'Tomlin', 'mike.tomlin@example.com', 0x01, 'NFLAdmin'),
('Andy', 'Reid', 'andy.reid@example.com', 0x01, 'NFLAdmin');
GO

-- STEP 4: NFLFan & NFLAdmin
INSERT INTO NFLFan (NFLFanID) VALUES (1), (2), (3), (4);
INSERT INTO NFLAdmin (NFLAdminID) VALUES (5), (6), (7), (8);
GO

-- STEP 5: FanTeam
INSERT INTO FanTeam (NFLFanID, TeamID, PrimaryTeam) VALUES
(1, 11, 1),   -- Tom Brady: Patriots
(1, 24, 0),   -- Tom Brady: Buccaneers
(2, 19, 1),   -- Aaron Rodgers: Packers
(2, 12, 0),   -- Aaron Rodgers: Jets
(2, 4, 0),    -- Aaron Rodgers: Steelers
(3, 23, 1),   -- Drew Brees: Saints
(3, 16, 0),   -- Drew Brees: Chargers
(4, 14, 1);   -- Patrick Mahomes: Chiefs
GO

-- STEP 6: Stadium (Sample)
INSERT INTO Stadium (StadiumName, StadiumCityState, Capacity) VALUES
('Gillette Stadium', 'Foxborough, MA', 65878),
('MetLife Stadium', 'East Rutherford, NJ', 82500),
('Lambeau Field', 'Green Bay, WI', 81441),
('Arrowhead Stadium', 'Kansas City, MO', 76416),
('AT&T Stadium', 'Arlington, TX', 80000),
('Levis Stadium', 'Santa Clara, CA', 68500),
('Lumen Field', 'Seattle, WA', 69000),
('SoFi Stadium', 'Inglewood, CA', 70240);
GO

-- STEP 7: TeamStadium (Sample)
INSERT INTO TeamStadium (TeamID, StadiumID, StartYear, EndYear) VALUES
(11, 1, 2002, NULL),   -- Patriots at Gillette
(12, 2, 2010, NULL),   -- Jets at MetLife
(19, 3, 1957, NULL),   -- Packers at Lambeau
(14, 4, 1972, NULL),   -- Chiefs at Arrowhead
(25, 5, 2009, NULL),   -- Cowboys at AT&T
(31, 6, 2014, NULL),   -- 49ers at Levi's
(32, 7, 2002, NULL),   -- Seahawks at Lumen
(30, 8, 2020, NULL);   -- Rams at SoFi
GO

-- STEP 8: Game (Sample Playoff Games)
INSERT INTO Game (GameRound, GameDate, GameStartTime, HomeTeamID, AwayTeamID, StadiumID, HomeTeamScore, AwayTeamScore, WinningTeamID) VALUES
('Wild Card', '2026-01-10', '16:30:00', 22, 30, 8, 31, 34, 30),
('Wild Card', '2026-01-10', '20:00:00', 17, 19, 3, 21, 27, 19),
('Divisional', '2026-01-17', '16:30:00', 14, 11, 4, 33, 30, 14),
('Divisional', '2026-01-17', '20:00:00', 32, 31, 7, 41, 6, 32);
GO

-- STEP 9: AdminChangesTracker
INSERT INTO AdminChangesTracker (NFLAdminID, GameID, ChangeType, ChangeDescription) VALUES
(5, 1, 'Insert', 'Bill Belichick scheduled Wild Card game'),
(6, 2, 'Insert', 'Sean McVay scheduled Wild Card game'),
(7, 3, 'Insert', 'Mike Tomlin scheduled Divisional game'),
(8, 4, 'Insert', 'Andy Reid scheduled Divisional game');
GO

-- VERIFICATION QUERIES
SELECT 'ConferenceDivision' AS TableName, COUNT(*) AS Count FROM ConferenceDivision
UNION ALL SELECT 'Team', COUNT(*) FROM Team
UNION ALL SELECT 'AppUser', COUNT(*) FROM AppUser
UNION ALL SELECT 'NFLFan', COUNT(*) FROM NFLFan
UNION ALL SELECT 'NFLAdmin', COUNT(*) FROM NFLAdmin
UNION ALL SELECT 'FanTeam', COUNT(*) FROM FanTeam;
GO

-- TEST STORED PROCEDURE
EXEC procGetTeamsForSpecifiedFan @Email = 'tom.brady@example.com';
GO


-- select * from AdminChangesTracker
-- select * from Game
-- select N.NFLAdminID, U.Firstname, U.LastName from NFLAdmin N inner join APPUser U on N.NFLAdminID = U.AppUserID

-- =============================================
-- CONFERENCE CHAMPIONSHIPS  (January 25, 2026)
-- =============================================

-- AFC Championship: (2) New England Patriots at (1) Denver Broncos
-- Patriots win 10-7
/*
    @GameRound = 'Conference',
    @HomeTeamID = 13, -- Denver Broncos
    @AwayTeamID = 11, -- New England Patriots
    @GameDate = '2026-01-25',
    @GameStartTime = '15:00',
    @StadiumID = 13, -- Empower Field at Mile High
    @NFLAdminID = 5; -- Bill Belichick


    @GameID = 11, 
    @HomeTeamScore = 7,
    @AwayTeamScore = 10,
    @NFLAdminID = 6; -- Sean McVay
*/


-- NFC Championship: (5) LA Rams at (1) Seattle Seahawks
-- Seahawks win 31-27
/*
    @GameRound = 'Conference',
    @HomeTeamID = 32, -- Seattle Seahawks
    @AwayTeamID = 30, -- LA Rams
    @GameDate = '2026-01-25',
    @GameStartTime = '18:30',
    @StadiumID = 30, -- Lumen Field
    @NFLAdminID = 6; -- Sean McVay

    @GameID = 12,
    @HomeTeamScore = 31,
    @AwayTeamScore = 27,
    @NFLAdminID = 7; -- Mike Tomlin
*/

-- =============================================
-- SUPER BOWL LX  (February 8, 2026)
-- Levi's Stadium, Santa Clara, CA (neutral site)
-- NFC designated home team per rotation
-- Seahawks win 29-13
-- =============================================

/*
    @GameRound = 'Super Bowl',
    @HomeTeamID = 32, -- Seattle Seahawks (NFC champion, designated home team)
    @AwayTeamID = 11, -- New England Patriots (AFC champion)
    @GameDate = '2026-02-08',
    @GameStartTime = '18:30',
    @StadiumID = 29, -- Levi's Stadium (neutral site)
    @NFLAdminID = 5; -- Bill Belichick

    @GameID = 13,  
    @HomeTeamScore = 29,
    @AwayTeamScore = 13,
    @NFLAdminID = 8; -- Mike Tomlin

*/

