-- Create a database for NFL app
--use master;

-- CREATE DATABASE MIST353_NFL_RDB_Williams;

-- DROP database MIST353_NFL_RDB_Williams;

use MIST353_NFL_RDB_Williams;

-- Create tables for first iteration


create TABLE ConferenceDivision (
    ConferenceDivisionID INT Identity(1,1)
        constraint PK_ConferenceDivision PRIMARY KEY,
    Conference NVARCHAR(50) NOT NULL,
        constraint CHK_Conference CHECK (Conference IN ('AFC','NFC')),
    Division NVARCHAR(50) NOT NULL
        constraint CHK_Division CHECK (Division IN ('East','North','South','West'))
);

GO

create TABLE Team (
    TeamID INT Identity(1,1) 
        constraint PK_Team PRIMARY KEY,
    TeamName VARCHAR(50) NOT NULL,
    TeamCityState NVARCHAR(50) NOT NULL,
    TeamColors NVARCHAR(50) NOT NULL,
    ConferenceDivisionID INT NOT NULL,
        Constraint FK_Team_ConferenceDivisionID FOREIGN KEY (ConferenceDivisionID) REFERENCES ConferenceDivision(ConferenceDivisionID)
);
