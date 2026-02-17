USE MIST353_NFL_RDB_Williams;
GO

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


-- Insert AFC North teams (4 rows)
INSERT INTO Team (TeamName, TeamCityState, TeamColors, ConferenceDivisionID) VALUES
    ('Baltimore Ravens', 'Baltimore, MD', 'Purple, Black, Gold', 2),
    ('Cincinnati Bengals', 'Cincinnati, OH', 'Black, Orange, White', 2),
    ('Cleveland Browns', 'Cleveland, OH', 'Brown, Orange, White', 2),
    ('Pittsburgh Steelers', 'Pittsburgh, PA', 'Black, Gold', 2);

