# Architecture

The pipeline is organized into five sequential stages:

1. **Extract** reads the customer and order CSV files and product JSON file from
   `data/`, then writes staged copies under `data/staging/`.
2. **Validate** checks required fields, identifiers, dates, and numeric values.
   Validated records are written under `data/validated/`; invalid records should
   be reported rather than silently discarded.
3. **Transform** normalizes the records and prepares customer, product, date,
   and sales datasets under `data/transformed/`.
4. **Load** loads dimensions before the sales fact table in PostgreSQL.
5. **Quality check** verifies the loaded records and relationships.

The intended fact grain is one row per order line (`order_item_id`). `FactSales`
references customer, product, and date dimensions. The SQL scripts create the
schema, reporting views, and indexes respectively.

The Python modules and DAG are starter code: each ETL operation raises
`NotImplementedError` until its TODO is implemented. The sample files establish
the expected source fields and referential relationships.
