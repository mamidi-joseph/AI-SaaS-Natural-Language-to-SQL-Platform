USE nl;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    signup_date DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (name, email, city, signup_date)
VALUES
('Ravi Kumar', 'ravi@mail.com', 'Chennai', '2024-01-15'),
('Priya Singh', 'priya@mail.com', 'Bangalore', '2024-02-20'),
('Arjun Mehta', 'arjun@mail.com', 'Mumbai', '2024-03-05'),
('Sneha Rao', 'sneha@mail.com', 'Chennai', '2024-04-10'),
('Karan Patel', 'karan@mail.com', 'Delhi', '2024-05-01');

INSERT INTO products (name, category, price)
VALUES
('Wireless Mouse', 'Electronics', 599.00),
('Office Chair', 'Furniture', 4999.00),
('Notebook Set', 'Stationery', 199.00),
('Bluetooth Speaker', 'Electronics', 1499.00),
('Desk Lamp', 'Furniture', 899.00);

INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES
(1, 1, 2, '2024-06-01'),
(2, 4, 1, '2024-06-03'),
(3, 2, 1, '2024-06-05'),
(1, 3, 5, '2024-06-10'),
(4, 5, 1, '2024-06-12'),
(5, 1, 1, '2024-06-15'),
(2, 2, 1, '2024-06-18');
