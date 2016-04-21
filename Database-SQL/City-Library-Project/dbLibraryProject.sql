CREATE DATABASE dbLibrary
GO

USE dbLibrary
GO

CREATE TABLE Book
(
BookId int PRIMARY KEY NOT NULL,
Title varchar (50) NOT NULL,
PublisherName varchar (50) NOT NULL
)
GO

CREATE TABLE Book_Authors
(
BookId int PRIMARY KEY NOT NULL,
AuthorName varchar (50) NOT NULL
)
GO

CREATE TABLE Publisher
(
Name varchar (50) PRIMARY KEY NOT NULL,
[Address] varchar (100),
Phone varchar (25) NOT NULL
)
GO

CREATE TABLE Book_Copies
(
BookId int NOT NULL,
BranchId int NOT NULL,
No_Of_Copies int NOT NULL
)
GO

CREATE TABLE Book_Loans
(
BookId int NOT NULL,
BranchId int NOT NULL,
CardNo int NOT NULL,
DateOut date NOT NULL, --date data type needs to be entered as YYYY-MM-DD.
DueDate date NOT NULL
)
GO

CREATE TABLE Library_Branch
(
BranchId int PRIMARY KEY NOT NULL,
BranchName varchar (50) NOT NULL,
[Address] varchar (100)
)
GO

CREATE TABLE Borrower
(
CardNo int PRIMARY KEY NOT NULL,
Name varchar (50) NOT NULL,
[Address] varchar (100),
Phone varchar (25) NOT NULL
)
GO

INSERT INTO Book
VALUES (1, 'The Lost Tribe', 'Smith Publishing House'),
(2, 'What Makes Me Tick?', 'HarperCollins'),
(3, 'Best Guess', 'Penguin Random House'),
(4, 'Whodathunkit', 'Simon & Schuster'),
(5, 'Prison Blues', 'HarperCollins'),
(6, 'Coffee Talk', 'Smith Publishing House'),
(7, 'NYY:  2016 and Beyond', 'HarperCollins'),
(8, 'Sid the Kid', 'Penguin Random House'),
(9, 'Denver Broncos - SB Champs', 'Simon & Schuster'),
(10, 'Best Book Ever', 'Simon & Schuster'),
(11, 'Great BBQ', 'Penguin Random House'),
(12, 'Hunting Tips', 'Simon & Schuster'),
(13, 'Your Grandma Owns a Mac', 'Penguin Random House'),
(14, 'IT', 'HarperCollins'),
(15, 'A Game of Thrones', 'Penguin Random House'),
(16, 'A Storm of Swords', 'Penguin Random House'),
(17, 'A Feast of Crows', 'Penguin Random House'),
(18, 'A Dance of Dragons', 'Penguin Random House'),
(19, 'A Clash of Kings', 'Penguin Random House'),
(20, 'The Winds of Winter', 'Penguin Random House')
GO

INSERT INTO Publisher
VALUES ('Smith Publishing House', 'PO Box 123', '503-123-5555'),
('Penguin Random House', '1331 1st Street Portland OR 97124', '503-234-5555'),
('Simon & Schuster', '333 2nd Ave Clackamas OR 97015', '503-354-555'),
('HarperCollins', '444 3rd Ave Portland OR 97232', '503-555-5555')
GO

INSERT INTO Book_Authors
VALUES (1, 'H.A. Ware Thayat'),
(2, 'Tim E. Balm'),
(3, 'John Doe'),
(4, 'Weird Al Yankovic'),
(5, 'Hillary Rodham Clinton'),
(6, 'Star R. Bucks'),
(7, 'JayZ'),
(8, 'Darius Kasparaitis'),
(9, 'John Elway'),
(10, 'Josephine Swenson'),
(11, 'Paul Mannen'),
(12, 'Doant Shute Yerself'),
(13, 'Bill Gates'),
(14, 'Stephen King'),
(15, 'George RR Martin'),
(16, 'George RR Martin'),
(17, 'George RR Martin'),
(18, 'George RR Martin'),
(19, 'George RR Martin'),
(20, 'George RR Martin')
GO

INSERT INTO Library_Branch
VALUES (1, 'Sharpstown', '123 5th Ave Portland OR 97233'),
(2, 'Central', '111 Main Street Lake Oswego 97035'),
(3, 'Evergreen', '122 4th Street Tualatin OR 97123'),
(4, 'Orchard', '111 7th Ave Canby OR 97013')
GO



INSERT INTO Book_Copies
VALUES (1, 1, 10),
(1, 2, 10),
(1, 3, 10),
(1, 4, 10),
(2, 1, 10),
(2, 2, 10),
(2, 3, 10),
(2, 4, 10),
(3, 1, 10),
(3, 2, 10),
(3, 3, 10),
(3, 4, 10),
(4, 1, 10),
(4, 2, 10),
(4, 3, 10),
(4, 4, 10),
(5, 1, 10),
(5, 2, 10),
(5, 3, 10),
(5, 4, 10),
(6, 1, 10),
(6, 2, 10),
(6, 3, 10),
(6, 4, 10),
(7, 1, 10),
(7, 2, 10),
(7, 3, 10),
(7, 4, 10),
(8, 1, 10),
(8, 2, 10),
(8, 3, 10),
(8, 4, 10),
(9, 1, 10),
(9, 2, 10),
(9, 3, 10),
(9, 4, 10),
(10, 1, 10),
(10, 2, 10),
(10, 3, 10),
(10, 4, 10),
(11, 1, 10),
(11, 2, 10),
(11, 3, 10),
(11, 4, 10),
(12, 1, 10),
(12, 2, 10),
(12, 3, 10),
(12, 4, 10),
(13, 1, 10),
(13, 2, 10),
(13, 3, 10),
(13, 4, 10),
(14, 1, 10),
(14, 2, 10),
(14, 3, 10),
(14, 4, 10),
(15, 1, 10),
(15, 2, 10),
(15, 3, 10),
(15, 4, 10),
(16, 1, 10),
(16, 2, 10),
(16, 3, 10),
(16, 4, 10),
(17, 1, 10),
(17, 2, 10),
(17, 3, 10),
(17, 4, 10),
(18, 1, 10),
(18, 2, 10),
(18, 3, 10),
(18, 4, 10),
(19, 1, 10),
(19, 2, 10),
(19, 3, 10),
(19, 4, 10),
(20, 1, 10),
(20, 2, 10),
(20, 3, 10),
(20, 4, 10)
GO

INSERT INTO Borrower
VALUES (1, 'John Smith', '321 S 1st Ave Tigard OR 97223', '503-321-5555'),
(2, 'Rebecca Brown', '432 S 2nd Ave Tigard OR 97223', '503-432-5555'),
(3, 'David Buckam', '543 S 3rd Ave Tualatin OR 97224', '503-667-5555'),
(4, 'Chad Johnson', '765 N 5th Ave Sherwood OR 97036', '503-987-5555'),
(5, 'Henry Ford', '908 W 7th Ave Wilsonville OR 97014', '503-888-5555'),
(6, 'Betty White', '807 E 3rd Street Salem OR 97333', '503-777-5555'),
(7, 'Edward Murphy', '342 W Beverly Blvd Woodburn OR 97555', '503-444-5555'),
(8, 'Ben Jammin', '655 N Franklin Ave Portland OR 97232', '503-333-5555'),
(9, 'Patty Locke', '555 E Pinstripe Lane Portland OR 97233', '503-222-5555'),
(10, 'Barbara McClane', '346 N 5th Ave Portland OR 97124', '503-999-5555')
GO

INSERT INTO Book_Loans
VALUES (1, 1, 1, '2016-02-01', '2016-03-01'),
(2, 1, 1, '2016-02-01', '2016-03-01'),
(3, 1, 1, '2016-02-01', '2016-03-01'),
(4, 1, 1, '2016-02-01', '2016-03-01'),
(5, 1, 1, '2016-02-01', '2016-03-01'),
(6, 1, 1, '2016-02-01', '2016-03-01'),
(7, 1, 1, '2016-02-01', '2016-03-01'),
(8, 1, 1, '2016-02-01', '2016-03-01'),
(9, 1, 1, '2016-02-01', '2016-03-01'),
(10, 1, 1, '2016-02-01', '2016-03-01'),
(11, 1, 1, '2016-02-01', '2016-03-01'),
(10, 2, 2, '2016-02-02', '2016-03-02'),
(11, 2, 2, '2016-02-02', '2016-03-02'),
(12, 2, 2, '2016-02-02', '2016-03-02'),
(13, 2, 2, '2016-02-02', '2016-03-02'),
(14, 2, 2, '2016-02-02', '2016-03-02'),
(15, 2, 2, '2016-02-02', '2016-03-02'),
(16, 2, 2, '2016-02-02', '2016-03-02'),
(17, 2, 2, '2016-02-02', '2016-03-02'),
(18, 2, 2, '2016-02-02', '2016-03-02'),
(19, 2, 3, '2016-02-03', '2016-03-03'),
(20, 2, 3, '2016-02-03', '2016-03-03'),
(1, 3, 4, '2016-02-07', '2016-03-07'),
(2, 3, 4, '2016-02-07', '2016-03-07'),
(3, 3, 4, '2016-02-07', '2016-03-07'),
(4, 3, 4, '2016-02-07', '2016-03-07'),
(5, 3, 4, '2016-02-07', '2016-03-07'),
(6, 3, 4, '2016-02-07', '2016-03-07'),
(7, 3, 4, '2016-02-07', '2016-03-07'),
(8, 3, 4, '2016-02-07', '2016-03-07'),
(9, 4, 5, '2016-02-08', '2016-03-08'),
(10, 4, 5, '2016-02-08', '2016-03-08'),
(11, 4, 5, '2016-02-08', '2016-03-08'),
(10, 4, 5, '2016-02-08', '2016-03-08'),
(11, 4, 5, '2016-02-08', '2016-03-08'),
(12, 4, 5, '2016-02-08', '2016-03-08'),
(13, 4, 6, '2016-02-09', '2016-03-09'),
(14, 4, 6, '2016-02-09', '2016-03-09'),
(15, 4, 6, '2016-02-09', '2016-03-09'),
(16, 4, 6, '2016-02-09', '2016-03-09'),
(17, 4, 6, '2016-02-09', '2016-03-09'),
(18, 3, 7, '2016-02-10', '2016-03-10'),
(19, 3, 7, '2016-02-10', '2016-03-10'),
(20, 3, 7, '2016-02-10', '2016-03-10'),
(11, 1, 1, '2016-02-11', '2016-03-11'),
(12, 1, 1, '2016-02-11', '2016-03-11'),
(13, 1, 1, '2016-02-11', '2016-03-11'),
(14, 1, 1, '2016-02-11', '2016-03-11'),
(15, 1, 1, '2016-02-11', '2016-03-11'),
(16, 1, 1, '2016-02-11', '2016-03-11'),
(17, 1, 1, '2016-02-11', '2016-03-11'),
(18, 1, 1, '2016-02-11', '2016-03-11'),
(19, 1, 1, '2016-02-11', '2016-03-11'),
(20, 1, 1, '2016-02-11', '2016-03-11'),
(20, 2, 8, '2015-11-01', '2015-12-01')
GO

--1) How many copies of the book titled The Lost Tribe are owned by the library branch
--whose name is "Sharpstown"?

SELECT DISTINCT LB.BranchName, B.Title, BC.No_Of_Copies
FROM Book AS B
INNER JOIN Book_Copies AS BC
ON BC.BookId = B.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId = BC.BranchId
WHERE B.Title = 'The Lost Tribe'
AND LB.BranchName = 'Sharpstown'
GO

--2) How many copies of the book titled 'The Lost Tribe' are owned by each library branch?

SELECT DISTINCT LB.BranchName, B.Title, BC.No_Of_Copies
FROM Book AS B
INNER JOIN Book_Copies AS BC
ON B.BookId = BC.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId = BC.BranchId
WHERE B.Title = 'The Lost Tribe'
GO

--3) Retrieve the names of all borrowers who do not have any books checked out.

SELECT DISTINCT Bor.Name, Bor.CardNo, BL.BookId, BL.DateOut, BL.DueDate
FROM Borrower AS Bor
INNER JOIN Book_Loans AS BL
ON Bor.CardNo = BL.CardNo
WHERE BL.DueDate < '2016-02-15'
GO

--I'm assuming that he has returned the book as we are not yet tracking 'past due/late returns'.
--It would probably be more appropriate to eventually add an additional column for 'DateIn' to
--avoid confusion and assist in identifying books 'past due'.

--4) For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today,
--Retrieve the book title, the borrower's name, and the borrower's address.

SELECT B.Title, Bor.Name, Bor.[Address]
FROM Borrower AS Bor
INNER JOIN Book_Loans AS BL
ON Bor.CardNo = BL.CardNo
INNER JOIN Library_Branch AS LB
ON LB.BranchId = BL.BranchId
INNER JOIN Book AS B
ON B.BookId = BL.BookId
WHERE BL.DueDate = '2016-02-15'
AND LB.BranchName = 'Sharpstown'
GO

--Since there are no books loaned out from Sharpstown that are due back today the result is 'empty'.
--Just for illustration below is the books due back on March 1st, 2016 at the Sharpstown branch.
--John Smith got a little carried away checking out books for himself and his family.

SELECT B.Title, Bor.Name, Bor.[Address]
FROM Borrower AS Bor
INNER JOIN Book_Loans AS BL
ON Bor.CardNo = BL.CardNo
INNER JOIN Library_Branch AS LB
ON LB.BranchId = BL.BranchId
INNER JOIN Book AS B
ON B.BookId = BL.BookId
WHERE BL.DueDate = '2016-03-01'
AND LB.BranchName = 'Sharpstown'
GO

--5) For each library branch, retrieve the branch name and the total number of books loaned out
--from that branch.

SELECT LB.BranchName, COUNT(*) AS No_of_Books_Checked_Out
FROM Book_Loans AS BL
INNER JOIN Library_Branch AS LB
ON BL.BranchId = LB.BranchId
WHERE BL.DueDate > '2016-02-14'
GROUP BY LB.BranchName
GO

--6) Retrieve the names, addresses, and number of books checked out for all borrowers who have more
--than five books checked out.

SELECT Bor.Name, Bor.[Address], COUNT(*) AS No_of_Books_Checked_Out
FROM Book_Loans AS BL
INNER JOIN Borrower as Bor
ON BL.CardNo = Bor.CardNo
WHERE BL.DueDate > '2016-02-14'
Group BY Bor.Name, Bor.[Address]
HAVING COUNT(*)>5
GO

--We have some real speed readers in the area, especially John Smith.

--7) For each book authored (or co-authored) by "Stephen King", retrieve the title and the number
--of copies owned by the library branch whose name is "Central".

SELECT DISTINCT B.Title, BC.No_Of_Copies
FROM Book AS B
INNER JOIN Book_Copies AS BC
ON B.BookId = BC.BookId
INNER JOIN Library_Branch AS LB
ON LB.BranchId = BC.BranchId
INNER JOIN Book_Authors AS BA
ON BA.BookId = B.BookId
WHERE BA.AuthorName = 'Stephen King'
AND LB.BranchName = 'Central'
GO

--Now, create a stored procedure that will execute one or more of those queries, based on user choice.
--See below for stored procedure and example EXEC.

CREATE PROCEDURE uspGetCopiesPerBranchByTitle @Title Varchar(50)
AS
	SELECT DISTINCT LB.BranchName, B.Title, BC.No_Of_Copies
	FROM Book AS B
	INNER JOIN Book_Copies AS BC
	ON B.BookId = BC.BookId
	INNER JOIN Library_Branch AS LB
	ON LB.BranchId = BC.BranchId
	WHERE B.Title = @Title
GO

EXEC uspGetCopiesPerBranchByTitle 'Great BBQ'
GO