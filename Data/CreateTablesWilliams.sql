/*
-- Create a database for NFL app
--use master;

-- CREATE DATABASE MIST353_NFL_RDB_Williams;

-- DROP database MIST353_NFL_RDB_Williams;

use MIST353_NFL_RDB_Williams;


-- Create ConferenceDivision table
CREATE TABLE ConferenceDivision (
    ConferenceDivisionID INT IDENTITY(1,1) CONSTRAINT PK_ConferenceDivision PRIMARY KEY,
    Conference NVARCHAR(50) NOT NULL CONSTRAINT CHK_Conference CHECK (Conference IN ('AFC', 'NFC')),
    Division NVARCHAR(50) NOT NULL CONSTRAINT CHK_Division CHECK (Division IN ('East', 'North', 'South', 'West')),
    CONSTRAINT UK_ConferenceDivision UNIQUE (Conference, Division)
);
GO


-- Create Team table
CREATE TABLE Team (
    TeamID INT IDENTITY(1,1) CONSTRAINT PK_Team PRIMARY KEY,
    TeamName NVARCHAR(50) NOT NULL,
    TeamCityState NVARCHAR(50) NOT NULL,
    TeamColors NVARCHAR(50) NOT NULL,
    ConferenceDivisionID INT NOT NULL,
    CONSTRAINT FK_Team_ConferenceDivisionID FOREIGN KEY (ConferenceDivisionID) REFERENCES ConferenceDivision(ConferenceDivisionID)
);
GO
*/

alter table ConferenceDivision
    NOCHECK CONSTRAINT CK_ConferenceNames;

alter table ConferenceDivision
    CHECK CONSTRAINT CK_ConferenceNames;


go

-- Create the database user (mapped to the existing login)
CREATE USER NandaSurendra
FOR LOGIN NandaSurendra;

-- Grant EXECUTE permission
GRANT EXECUTE TO NandaSurendra;

-- Grant SELECT permission (read access)
GRANT SELECT TO NandaSurendra;



CREATE TABLE AppUser (
    AppUserID INT IDENTITY(1,1) PRIMARY KEY,
    Firstname NVARCHAR(50) NOT NULL,
    Lastname NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    PasswordHash VARBINARY(200) NOT NULL,
    UserRole NVARCHAR(50) NOT NULL
);
GO
