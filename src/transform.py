"""Transform validated source records into star-schema datasets."""

from pathlib import Path


def transform_customers(source_path: Path, output_path: Path) -> Path:
    """Map validated customer records to the DimCustomer load format."""
    # TODO: Normalize customer attributes and map them to the dimension columns.
    raise NotImplementedError("Customer transformation has not been implemented.")


def transform_products(source_path: Path, output_path: Path) -> Path:
    """Map validated product records to the DimProduct load format."""
    # TODO: Normalize product attributes and map them to the dimension columns.
    raise NotImplementedError("Product transformation has not been implemented.")


def transform_orders(source_path: Path, output_path: Path) -> Path:
    """Map validated order lines to the FactSales load format."""
    # TODO: Resolve dimension keys and calculate each order line's sales amount.
    raise NotImplementedError("Order transformation has not been implemented.")


def transform_all(validated_dir: Path, transformed_dir: Path) -> dict[str, Path]:
    """Transform all validated files and return output paths by entity."""
    # TODO: Build the date dimension, transform each entity, and prepare fact rows.
    raise NotImplementedError("Pipeline transformation has not been implemented.")
