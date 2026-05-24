-- Write your query below
-- join on id 
-- then get the volume via width length height
-- group by warehouse_name

SELECT
    w.name AS warehouse_name,
    SUM(w.units * p.width * p.length * p.height) AS volume

FROM warehouse w
JOIN products p on w.product_id = p.product_id
GROUP BY w.name;

