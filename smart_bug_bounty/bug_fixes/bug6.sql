CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount DECIMAL(10, 2),
    status VARCHAR(20)
);

INSERT INTO orders (id, customer_id, amount, status)
VALUES
    (1, 101, 50.00, 'paid'),
    (2, 101, 25.00, 'pending'),
    (3, 102, 80.00, 'paid');

SELECT customer_id, SUM(amount) AS total_spent
FROM orders
WHERE status = 'paid'
GROUP BY customer_id
HAVING total_spent > 60
ORDER BY total_spent DESC;
