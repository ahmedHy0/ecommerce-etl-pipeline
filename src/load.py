"""Load transformed datasets into the PostgreSQL star schema."""

from pathlib import Path

from sqlalchemy.engine import Engine


def load_customers(source_path: Path, engine: Engine) -> int:
    """Load customer dimension records and return the number of rows loaded."""
    # TODO: Upsert records into DimCustomer and return the affected row count.
    raise NotImplementedError("Customer dimension loading has not been implemented.")


def load_products(source_path: Path, engine: Engine) -> int:
    """Load product dimension records and return the number of rows loaded."""
    # TODO: Upsert records into DimProduct and return the affected row count.
    raise NotImplementedError("Product dimension loading has not been implemented.")


def load_dates(source_path: Path, engine: Engine) -> int:
    """Load date dimension records and return the number of rows loaded."""
    # TODO: Insert missing DimDate rows and return the affected row count.
    raise NotImplementedError("Date dimension loading has not been implemented.")


def load_sales(source_path: Path, engine: Engine) -> int:
    """Load sales fact records and return the number of rows loaded."""
    # TODO: Load FactSales rows after their dimension keys are available.
    raise NotImplementedError("Sales fact loading has not been implemented.")


def load_all(transformed_dir: Path, database_url: str) -> int:
    """Load all transformed datasets and return the total number of rows loaded."""
    # TODO: Create an SQLAlchemy engine, load dimensions before facts, and dispose it.
    raise NotImplementedError("Pipeline loading has not been implemented.")


def run_quality_checks(database_url: str) -> None:
    """Raise an error if required post-load data-quality checks fail."""
    # TODO: Check fact/dimension integrity, required row counts, and sales totals.
    raise NotImplementedError("Post-load quality checks have not been implemented.")
