-- PostgreSQL star schema. Apply this script before loading pipeline data.

CREATE TABLE IF NOT EXISTS "DimCustomer" (
    customer_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id VARCHAR(50) NOT NULL UNIQUE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "DimProduct" (
    product_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id VARCHAR(50) NOT NULL UNIQUE,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    list_price NUMERIC(12, 2) NOT NULL CHECK (list_price >= 0)
);

CREATE TABLE IF NOT EXISTS "DimDate" (
    date_key INTEGER PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,
    year SMALLINT NOT NULL,
    quarter SMALLINT NOT NULL CHECK (quarter BETWEEN 1 AND 4),
    month SMALLINT NOT NULL CHECK (month BETWEEN 1 AND 12),
    day_of_month SMALLINT NOT NULL CHECK (day_of_month BETWEEN 1 AND 31),
    day_name VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS "FactSales" (
    sales_key BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_item_id VARCHAR(50) NOT NULL UNIQUE,
    order_id VARCHAR(50) NOT NULL,
    customer_key BIGINT NOT NULL REFERENCES "DimCustomer" (customer_key),
    product_key BIGINT NOT NULL REFERENCES "DimProduct" (product_key),
    date_key INTEGER NOT NULL REFERENCES "DimDate" (date_key),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12, 2) NOT NULL CHECK (unit_price >= 0),
    sales_amount NUMERIC(14, 2) NOT NULL CHECK (sales_amount >= 0)
);
