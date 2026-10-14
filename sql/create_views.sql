-- Read-only reporting views over the star schema.

CREATE OR REPLACE VIEW "vw_SalesByDate" AS
SELECT
    d.full_date,
    d.year,
    d.month,
    SUM(f.quantity) AS units_sold,
    SUM(f.sales_amount) AS total_sales
FROM "FactSales" AS f
JOIN "DimDate" AS d ON d.date_key = f.date_key
GROUP BY d.full_date, d.year, d.month;

CREATE OR REPLACE VIEW "vw_SalesByProduct" AS
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(f.quantity) AS units_sold,
    SUM(f.sales_amount) AS total_sales
FROM "FactSales" AS f
JOIN "DimProduct" AS p ON p.product_key = f.product_key
GROUP BY p.product_id, p.product_name, p.category;

CREATE OR REPLACE VIEW "vw_SalesByCustomer" AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country,
    COUNT(DISTINCT f.order_id) AS order_count,
    SUM(f.sales_amount) AS total_sales
FROM "FactSales" AS f
JOIN "DimCustomer" AS c ON c.customer_key = f.customer_key
GROUP BY c.customer_id, c.first_name, c.last_name, c.country;
