# E-Commerce ETL Pipeline

A starter project for extracting e-commerce source data, validating and
transforming it, loading a PostgreSQL star schema, and checking the loaded
data with Apache Airflow.

> **Starter-code status:** The ETL functions are intentionally not implemented.
> They contain `TODO` markers and raise `NotImplementedError`, so an Airflow
> run will fail visibly until the implementation work is completed.

## Project structure

```text
ecommerce-etl-pipeline/
├── data/
│   ├── raw_customers.csv
│   ├── raw_orders.csv
│   └── raw_products.json
├── dags/
│   └── ecommerce_etl_dag.py
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── validate.py
│   ├── transform.py
│   └── load.py
├── sql/
│   ├── create_star_schema.sql
│   ├── create_views.sql
│   └── create_indexes.sql
├── docs/
│   └── architecture.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Architecture

The Airflow DAG runs the following stages in order:

```text
Extract -> Validate -> Transform -> Load -> Quality Check
```

- **Extract** reads the CSV and JSON source files and prepares staged files.
- **Validate** checks required values, identifiers, dates, and numeric ranges.
- **Transform** prepares `DimCustomer`, `DimProduct`, `DimDate`, and `FactSales`
  datasets. The fact table grain is one row per order line.
- **Load** writes the dimensions and then the sales facts to PostgreSQL.
- **Quality Check** verifies loaded records and referential integrity.

Each stage has a module in `src/`. The DAG is in `dags/`; PostgreSQL DDL,
reporting views, and indexes are in `sql/`. More detail is in
[`docs/architecture.md`](docs/architecture.md).

## Sample data

The sample records are deliberately small and relationally consistent:

- Each order line references an existing customer and product.
- `order_item_id` uniquely identifies a line and is the intended sales-fact
  grain.
- Order dates and line prices are provided in `raw_orders.csv`; product
  attributes and list prices are provided in `raw_products.json`.

## Requirements

- Python 3.10–3.12
- PostgreSQL 13 or later
- Apache Airflow 2.10.5

Airflow is intended to run on Linux. On Windows, use WSL2 or a Linux container
for the Airflow environment. Use the official Airflow constraints file matching
both the Airflow and Python versions to install dependencies reliably; Airflow
has additional dependency constraints beyond a normal `pip install`.

For example, in a Linux or WSL2 shell with Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt \
  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.12.txt"
```

The constraints file pins Airflow and its dependencies to a compatible set
while installing the project's additional packages. Use the constraints file
matching the Python version in your environment.

## Database setup

Create a PostgreSQL database and user, then set the connection URL in the
environment where Airflow tasks will run:

```text
ECOMMERCE_DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/DATABASE
```

Do not commit credentials or a populated `.env` file. Before running the
pipeline for the first time, execute these scripts in order against the target
database:

1. `sql/create_star_schema.sql`
2. `sql/create_views.sql`
3. `sql/create_indexes.sql`

The database schema is PostgreSQL-specific. The starter loader expects the
connection URL as an argument; the DAG reads it from `ECOMMERCE_DATABASE_URL`
when the load and quality-check tasks execute.

## Configure and run Airflow

Set `AIRFLOW_HOME`, point Airflow at this project's DAG directory, and add the
project root to `PYTHONPATH` so that the DAG can import the `src` package. For
example, from the project root in a Linux or WSL2 shell:

```bash
export AIRFLOW_HOME="$PWD/.airflow"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export PYTHONPATH="$PWD"
export ECOMMERCE_DATABASE_URL="postgresql+psycopg2://USER:PASSWORD@HOST:5432/DATABASE"

airflow db migrate
airflow users create \
  --username admin \
  --firstname Pipeline \
  --lastname Admin \
  --role Admin \
  --email admin@example.com
airflow webserver --port 8080
```

In a second shell with the same environment, start the scheduler:

```bash
airflow scheduler
```

Open `http://localhost:8080`, enable `ecommerce_etl_pipeline`, and trigger a
run. Tasks intentionally fail with `NotImplementedError` until their
corresponding functions in `src/` have been implemented.

## Implementation checklist

1. Implement extraction and define the staging file format.
2. Implement validation, including explicit handling and reporting of invalid
   rows.
3. Implement transformations and generate a `DimDate` row for every fact date.
4. Implement idempotent dimension loading and load facts only after dimensions.
5. Implement quality checks and add tests for valid, invalid, and duplicate
   input records.
