CREATE DATABASE IF NOT EXISTS Employees;
USE Employees;

-- created employees table

CREATE TABLE Employees (
    employeeID INT PRIMARY KEY,
    firstName VARCHAR (50) NOT NULL,
    lastName VARCHAR (50) NOT NULL,
    department VARCHAR (40) NOT NULL,
    hireDate DATE
);

-- insert a few sample records

INSERT INTO Employees (employeeID, firstName, lastName, department, hireDate)
VALUES
    (001, 'Ashley', 'Ella', 'Marketing', '2023-03-21'),
    (002, 'Isabela', 'Merced', 'Business', '2024-04-03'),
    (003, 'Jenna', 'Ortega', 'ICT', '2022-09-23');

-- retrieve all employees

SELECT *
FROM Employees
WHERE hireDate > '2023-01-01'
ORDER BY lastName ASC;