CREATE DATABASE IF NOT EXISTS Orders;

USE Orders;

CREATE TABLE Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Students(customer_id)
);

INSERT INTO Orders
VALUES 
    (1, 101, '2018-05-15', 67.94),
    (2, 102, '2019-11-24', 570.18),
    (3, 103, '2020-03-20', 37.34);

SELECT *
FROM Orders
WHERE order_date = '2018-05-15';

SELECT 
O.order_id, 
S.first_name,
S.last_name,
S.email,
O.order_date,
O.total
FROM Orders O
JOIN Students S ON O.customer_id = S.students_id
WHERE O.customer_id = 101;

UPDATE Orders
SET total = 50.00
WHERE order_id = 3;

DELETE FROM Orders
WHERE order_id = 2;