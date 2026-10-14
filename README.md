<div align="center">

# E-Commerce Data Integration & Analytics Pipeline

An end-to-end modular Data Engineering pipeline designed to ingest multi-source e-commerce data, validate and transform records, load a PostgreSQL star schema, and orchestrate execution via Apache Airflow.

![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.10.5-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-ETL%20Pipeline-0EA5E9?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)

</div>

## Project Overview

This data engineering pipeline extracts multi-source e-commerce data (`CSV` and `JSON`), performs automated validation and cleaning, transforms the data into a dimensional star schema using Pandas, loads it into a PostgreSQL data warehouse, and uses Apache Airflow for complete workflow orchestration and data quality checks.

**Suggested GitHub topics:** `data-engineering`, `apache-airflow`, `etl-pipeline`, `postgresql`, `pandas`, `star-schema`, `python`, `data-integration`

## Key Features

- Multi-source data ingestion (API/CSV/JSON)
- Automated data quality validation and bad-row handling
- Clean Pandas transformations into a Star Schema (`DimCustomer`, `DimProduct`, `DimDate`, `FactSales`)
- Idempotent PostgreSQL loading layer
- Apache Airflow orchestration DAG (`Extract ➔ Validate ➔ Transform ➔ Load ➔ Quality Check`)
- Modular source-code architecture

## Architecture & Workflow

1. **Extract**: Reads raw files and prepares staged data sources.
2. **Validate**: Checks required fields, data types, identifiers, and ranges.
3. **Transform**: Generates dimension records and fact tables at the order-line grain.
4. **Load**: Performs idempotent upserts into PostgreSQL database tables.
5. **Quality Check**: Verifies loaded row counts and referential integrity.

## How It Works

1. **Extraction**: The Airflow DAG triggers the extraction module (`src/extract.py`), which reads raw customer, order, and product files from storage/sources and outputs them into standardized staging layers.
2. **Validation**: The validation module (`src/validate.py`) sweeps through the staged data to catch missing values, duplicate primary keys, invalid date formats, or out-of-range prices, isolating faulty rows.
3. **Transformation**: The transformation module (`src/transform.py`) uses Pandas to process clean records, map dimensions (`DimCustomer`, `DimProduct`, `DimDate`), and structure the `FactSales` table at the individual order-line grain.
4. **Database Loading**: The loader (`src/load.py`) executes idempotent upserts (`ON CONFLICT` constraints) into PostgreSQL, ensuring dimension tables are updated before inserting facts.
5. **Quality Assurance**: Final task checks are run to cross-verify foreign key constraints, row totals, and pipeline completeness before marking the DAG run successful.

## Tech Stack

| Technology | Role |
|---|---|
| Python | Core ETL programming language |
| Apache Airflow | Workflow scheduling and orchestration |
| PostgreSQL | Target analytical data warehouse (Star Schema) |
| Pandas | Data transformation and dataframe manipulation |
| Psycopg2 | PostgreSQL adapter for Python |

## Project Structure

```text
ecommerce-etl-pipeline/
├── data/
│   ├── raw_customers.csv
│   ├── raw_orders.csv
│   └── raw_products.json
├── dags/
│   └── ecommerce_etl_dag.py
├── docs/
│   └── architecture.md
├── sql/
│   ├── create_star_schema.sql
│   ├── create_views.sql
│   └── create_indexes.sql
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   └── load.py
├── .gitignore
├── requirements.txt
└── README.md

## Use Cases

- Automated batch data processing for e-commerce transactions
- Enterprise data warehousing using dimensional star schemas
- Pipeline orchestration and error handling demonstrations with Apache Airflow
- Academic graduation project (DEPI Data Engineering track)

## Team Members

- Amr Moustafa Amer
- Mohamed El sayed Mohammed
- Ahmed Hany Khairy
- Amr Mostafa Draz
- Mohamed Ali Ibrahim