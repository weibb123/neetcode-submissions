-- Write your query below
-- never placed an order -> id not in orders table -> but exist in customers table
SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders);