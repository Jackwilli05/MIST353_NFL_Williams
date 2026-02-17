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
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Buffalo Bills', 'Orchard Park, NY', 'Royal Blue, Red, White', 1),
    ('Miami Dolphins', 'Miami Gardens, FL', 'Aqua, Orange, White', 1),
    ('New England Patriots', 'Foxborough, MA', 'Navy Blue, Red, Silver', 1),
    ('New York Jets', 'East Rutherford, NJ', 'Gotham Green, White', 1);
GO

-- AFC North
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Baltimore Ravens', 'Baltimore, MD', 'Purple, Black, Gold', 2),
    ('Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange, White', 2),
    ('Cleveland Browns', 'Cleveland, OH', 'Brown, Orange, White', 2),
    ('Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Gold', 2);
GO

-- AFC South
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Houston Texans', 'Houston, TX', 'Deep Steel Blue, Battle Red, Liberty White', 3),
    ('Indianapolis Colts', 'Indianapolis, IN', 'Royal Blue, White', 3),
    ('Jacksonville Jaguars', 'Jacksonville, FL', 'Teal, Black, Gold', 3),
    ('Tennessee Titans', 'Nashville, TN', 'Navy Blue, Titans Blue, Red, Silver', 3);
GO

--AFC West
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Denver Broncos', 'Denver, CO', 'Orange, Navy Blue, White', 4),
    ('Kansas City Chiefs', 'Kansas City, MO', 'Red, Gold, White', 4),
    ('Las Vegas Raiders', 'Las Vegas, NV', 'Silver, Black', 4),
    ('Los Angeles Chargers', 'Inglewood, CA', 'Powder Blue, White, Gold', 4);
GO

--NFC East
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Dallas Cowboys', 'Arlington, TX', 'Navy Blue, Metallic Silver, White', 5),
    ('New York Giants', 'East Rutherford, NJ', 'Royal Blue, Red, White', 5),
    ('Philadelphia Eagles', 'Philadelphia, PA', 'Midnight Green, Silver, Black, White', 5),
    ('Washington Commanders', 'Landover, MD', 'Burgundy, Gold', 5);
GO

--NFC North
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Chicago Bears', 'Chicago, IL', 'Navy Blue, Orange', 6),
    ('Detroit Lions', 'Detroit, MI', 'Honolulu Blue, Silver', 6),
    ('Green Bay Packers', 'Green Bay, WI', 'Dark Green, Gold', 6),
    ('Minnesota Vikings', 'Minneapolis, MN', 'Purple, Gold, White', 6);
GO

-- NFC South 
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Atlanta Falcons', 'Atlanta, GA', 'Red, Black, Silver, White', 7),
    ('Carolina Panthers', 'Charlotte, NC', 'Black, Process Blue, Silver', 7),
    ('New Orleans Saints', 'New Orleans, LA', 'Old Gold, Black, White', 7),
    ('Tampa Bay Buccaneers', 'Tampa, FL', 'Pewter, Red, Bay Orange, White', 7);
GO

-- NFC West
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Arizona Cardinals', 'Glendale, AZ', 'Cardinal Red, White, Black', 8),
    ('Los Angeles Rams', 'Inglewood, CA', 'Royal Blue, Sol Yellow, White', 8),
    ('San Francisco 49ers', 'Santa Clara, CA', 'Scarlet Red, Metallic Gold', 8),
    ('Seattle Seahawks', 'Seattle, WA', 'College Navy, Action Green, Wolf Grey', 8);
GO



/*
--See all tables

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';
GO

-- See data in ConferenceDivision
SELECT * FROM ConferenceDivision;
GO

-- See data in Team
SELECT * FROM Team;
GO
*/



