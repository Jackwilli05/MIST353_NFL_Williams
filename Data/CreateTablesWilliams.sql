-- ============================================
-- DROP TABLES IN CORRECT ORDER
-- ============================================
DROP TABLE IF EXISTS AdminChangesTracker;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS TeamStadium;
DROP TABLE IF EXISTS Stadium;
DROP TABLE IF EXISTS FanTeam;
DROP TABLE IF EXISTS NFLAdmin;
DROP TABLE IF EXISTS NFLFan;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS ConferenceDivision;
DROP TABLE IF EXISTS AppUser;
GO

-- ============================================
-- CREATE TABLES
-- ============================================

CREATE TABLE ConferenceDivision (
    ConferenceDivisionID INT IDENTITY(1,1) PRIMARY KEY,
    Conference NVARCHAR(50) NOT NULL,
    Division NVARCHAR(50) NOT NULL,
    CONSTRAINT CK_Conference CHECK (Conference IN ('AFC', 'NFC')),
    CONSTRAINT CK_Division CHECK (Division IN ('East', 'North', 'South', 'West')),
    CONSTRAINT UK_ConferenceDivision UNIQUE (Conference, Division)
);
GO

CREATE TABLE Team (
    TeamID INT IDENTITY(1,1) PRIMARY KEY,
    TeamName NVARCHAR(50) NOT NULL,
    TeamCityState NVARCHAR(50) NOT NULL,
    TeamColors NVARCHAR(100) NOT NULL,
    ConferenceDivisionID INT NOT NULL,
    CONSTRAINT FK_Team_ConferenceDivision FOREIGN KEY (ConferenceDivisionID) REFERENCES ConferenceDivision(ConferenceDivisionID)
);
GO

CREATE TABLE AppUser (
    AppUserID INT IDENTITY(1,1) PRIMARY KEY,
    Firstname NVARCHAR(50) NOT NULL,
    Lastname NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARBINARY(200) NOT NULL,
    UserRole NVARCHAR(20) NOT NULL,
    CONSTRAINT CK_UserRole CHECK (UserRole IN ('NFLFan', 'NFLAdmin'))
);
GO

CREATE TABLE NFLFan (
    NFLFanID INT PRIMARY KEY,
    CONSTRAINT FK_NFLFan_AppUser FOREIGN KEY (NFLFanID) REFERENCES AppUser(AppUserID) ON DELETE CASCADE
);
GO

CREATE TABLE NFLAdmin (
    NFLAdminID INT PRIMARY KEY,
    CONSTRAINT FK_NFLAdmin_AppUser FOREIGN KEY (NFLAdminID) REFERENCES AppUser(AppUserID) ON DELETE CASCADE
);
GO

CREATE TABLE FanTeam (
    FanTeamID INT IDENTITY(1,1) PRIMARY KEY,
    NFLFanID INT NOT NULL,
    TeamID INT NOT NULL,
    PrimaryTeam BIT NOT NULL,
    CONSTRAINT FK_FanTeam_NFLFan FOREIGN KEY (NFLFanID) REFERENCES NFLFan(NFLFanID) ON DELETE CASCADE,
    CONSTRAINT FK_FanTeam_Team FOREIGN KEY (TeamID) REFERENCES Team(TeamID) ON DELETE CASCADE,
    CONSTRAINT UK_FanTeam UNIQUE (NFLFanID, TeamID)
);
GO

CREATE TABLE Stadium (
    StadiumID INT IDENTITY(1,1) PRIMARY KEY,
    StadiumName NVARCHAR(100) NOT NULL,
    StadiumCityState NVARCHAR(50) NOT NULL,
    Capacity INT NOT NULL
);
GO

CREATE TABLE TeamStadium (
    TeamStadiumID INT IDENTITY(1,1) PRIMARY KEY,
    TeamID INT NOT NULL,
    StadiumID INT NOT NULL,
    StartYear INT NOT NULL,
    EndYear INT NULL,
    CONSTRAINT FK_TeamStadium_Team FOREIGN KEY (TeamID) REFERENCES Team(TeamID),
    CONSTRAINT FK_TeamStadium_Stadium FOREIGN KEY (StadiumID) REFERENCES Stadium(StadiumID)
);
GO

CREATE TABLE Game (
    GameID INT IDENTITY(1,1) PRIMARY KEY,
    GameRound NVARCHAR(50) NOT NULL,
    GameDate DATE NOT NULL,
    GameStartTime TIME NOT NULL,
    HomeTeamID INT NOT NULL,
    AwayTeamID INT NOT NULL,
    StadiumID INT NOT NULL,
    HomeTeamScore INT NULL,
    AwayTeamScore INT NULL,
    WinningTeamID INT NULL,
    CONSTRAINT FK_Game_HomeTeam FOREIGN KEY (HomeTeamID) REFERENCES Team(TeamID),
    CONSTRAINT FK_Game_AwayTeam FOREIGN KEY (AwayTeamID) REFERENCES Team(TeamID),
    CONSTRAINT FK_Game_Stadium FOREIGN KEY (StadiumID) REFERENCES Stadium(StadiumID),
    CONSTRAINT FK_Game_WinningTeam FOREIGN KEY (WinningTeamID) REFERENCES Team(TeamID),
    CONSTRAINT CK_GameRound CHECK (GameRound IN ('Wild Card', 'Divisional', 'Conference', 'Super Bowl')),
    CONSTRAINT CK_Game_Teams CHECK (HomeTeamID != AwayTeamID)
);
GO

CREATE TABLE AdminChangesTracker (
    AdminChangesTrackerID INT IDENTITY(1,1) PRIMARY KEY,
    NFLAdminID INT NOT NULL,
    GameID INT NOT NULL,
    ChangeDateTime DATETIME NOT NULL DEFAULT GETDATE(),
    ChangeType NVARCHAR(50) NOT NULL,
    ChangeDescription NVARCHAR(500) NOT NULL,
    CONSTRAINT FK_AdminChangesTracker_NFLAdmin FOREIGN KEY (NFLAdminID) REFERENCES NFLAdmin(NFLAdminID),
    CONSTRAINT FK_AdminChangesTracker_Game FOREIGN KEY (GameID) REFERENCES Game(GameID),
    CONSTRAINT CK_ChangeType CHECK (ChangeType IN ('Insert', 'Update', 'Delete'))
);
GO

PRINT 'All tables created successfully!';