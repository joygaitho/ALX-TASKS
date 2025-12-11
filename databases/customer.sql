CREATE DATABASE IF NOT EXISTS Customers;

USE Customers;

SELECT full_name, email
FROM Customers;

SELECT prod_name, price
FROM Products
WHERE price > 50;

SELECT *
FROM Orders
WHERE order_date > '01-01-2023' AND order_status = 'Shipped';

SELECT prod_name, unit_price
FROM Products
WHERE unit_price > (SELECT AVG(unit_price) FROM Products);

SELECT department, COUNT(employee_id) AS total_employees
FROM Employees
GROUP BY department;