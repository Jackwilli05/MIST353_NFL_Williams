USE MIST353_NFL_RDB_Williams;
go

-- Insert all ConferenceDivision data (8 rows)
INSERT INTO ConferenceDivision (Conference, Division) VALUES
    ('AFC', 'East'),
    ('AFC', 'North'),
    ('AFC', 'South'),
    ('AFC', 'West'),
    ('NFC', 'East'),
    ('NFC', 'North'),
    ('NFC', 'South'),
    ('NFC', 'West');

-- AFC East
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (1, 'Buffalo Bills', 'Orchard Park, NY', 'Royal Blue, Red, White', 1),
    (2, 'Miami Dolphins', 'Miami Gardens, FL', 'Aqua, Orange, White', 1),
    (3, 'New England Patriots', 'Foxborough, MA', 'Navy Blue, Red, Silver', 1),
    (4, 'New York Jets', 'East Rutherford, NJ', 'Gotham Green, White', 1);
GO

-- AFC North
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (5, 'Baltimore Ravens', 'Baltimore, MD', 'Purple, Black, Gold', 2),
    (6, 'Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange, White', 2),
    (7, 'Cleveland Browns', 'Cleveland, OH', 'Brown, Orange, White', 2),
    (8, 'Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Gold', 2);
GO

-- AFC South
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (9, 'Houston Texans', 'Houston, TX', 'Deep Steel Blue, Battle Red, Liberty White', 3),
    (10, 'Indianapolis Colts', 'Indianapolis, IN', 'Royal Blue, White', 3),
    (11, 'Jacksonville Jaguars', 'Jacksonville, FL', 'Teal, Black, Gold', 3),
    (12, 'Tennessee Titans', 'Nashville, TN', 'Navy Blue, Titans Blue, Red, Silver', 3);
GO

--AFC West
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (13, 'Denver Broncos', 'Denver, CO', 'Orange, Navy Blue, White', 4),
    (14, 'Kansas City Chiefs', 'Kansas City, MO', 'Red, Gold, White', 4),
    (15, 'Las Vegas Raiders', 'Las Vegas, NV', 'Silver, Black', 4),
    (16, 'Los Angeles Chargers', 'Inglewood, CA', 'Powder Blue, White, Gold', 4);
GO

--NFC East
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (17, 'Dallas Cowboys', 'Arlington, TX', 'Navy Blue, Metallic Silver, White', 5),
    (18, 'New York Giants', 'East Rutherford, NJ', 'Royal Blue, Red, White', 5),
    (19, 'Philadelphia Eagles', 'Philadelphia, PA', 'Midnight Green, Silver, Black, White', 5),
    (20, 'Washington Commanders', 'Landover, MD', 'Burgundy, Gold', 5);
GO

--NFC North
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (21, 'Chicago Bears', 'Chicago, IL', 'Navy Blue, Orange', 6),
    (22, 'Detroit Lions', 'Detroit, MI', 'Honolulu Blue, Silver', 6),
    (23, 'Green Bay Packers', 'Green Bay, WI', 'Dark Green, Gold', 6),
    (24, 'Minnesota Vikings', 'Minneapolis, MN', 'Purple, Gold, White', 6);
GO

-- NFC South 
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (25, 'Atlanta Falcons', 'Atlanta, GA', 'Red, Black, Silver, White', 7),
    (26, 'Carolina Panthers', 'Charlotte, NC', 'Black, Process Blue, Silver', 7),
    (27, 'New Orleans Saints', 'New Orleans, LA', 'Old Gold, Black, White', 7),
    (28, 'Tampa Bay Buccaneers', 'Tampa, FL', 'Pewter, Red, Bay Orange, White', 7)
GO

-- NFC West
INSERT INTO Team (TeamID, TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    (29, 'Arizona Cardinals', 'Glendale, AZ', 'Cardinal Red, White, Black', 8),
    (30, 'Los Angeles Rams', 'Inglewood, CA', 'Royal Blue, Sol Yellow, White', 8),
    (31, 'San Francisco 49ers', 'Santa Clara, CA', 'Scarlet Red, Metallic Gold', 8),
    (32, 'Seattle Seahawks', 'Seattle, WA', 'College Navy, Action Green, Wolf Grey', 8);
GO


USE MIST353_NFL_RDB_Williams;
GO

-- See all tables in database
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';
GO

-- See all data in ConferenceDivision
SELECT * FROM ConferenceDivision;
GO

-- See all data in Team
SELECT * FROM Team;
GO

