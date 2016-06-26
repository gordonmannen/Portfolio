USE master
GO

IF EXISTS (SELECT * FROM sys.databases WHERE [name] = 'dbPens')
DROP DATABASE dbPens
GO

CREATE DATABASE dbPens
GO


USE dbPens
GO

CREATE TABLE Penguins
(StanleyCupChampions nvarchar(50), Year int, ConnSmytheTrophy nvarchar(50), Captain nvarchar(50))

SELECT * FROM Penguins