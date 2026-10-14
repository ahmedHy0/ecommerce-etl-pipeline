-- Indexes for common fact-table joins and reporting filters.

CREATE INDEX IF NOT EXISTS idx_factsales_customer_key
    ON "FactSales" (customer_key);

CREATE INDEX IF NOT EXISTS idx_factsales_product_key
    ON "FactSales" (product_key);

CREATE INDEX IF NOT EXISTS idx_factsales_date_key
    ON "FactSales" (date_key);

CREATE INDEX IF NOT EXISTS idx_factsales_order_id
    ON "FactSales" (order_id);
