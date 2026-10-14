"""Validate staged customer, order, and product records."""

from pathlib import Path


def validate_customers(source_path: Path, output_path: Path) -> Path:
    """Validate customer fields and write valid records to a new file."""
    # TODO: Check required fields, email format, and unique customer identifiers.
    raise NotImplementedError("Customer validation has not been implemented.")


def validate_orders(source_path: Path, output_path: Path) -> Path:
    """Validate order-line fields and write valid records to a new file."""
    # TODO: Check identifiers, dates, positive quantities, and non-negative prices.
    raise NotImplementedError("Order validation has not been implemented.")


def validate_products(source_path: Path, output_path: Path) -> Path:
    """Validate product fields and write valid records to a new file."""
    # TODO: Check required fields, unique product identifiers, and valid prices.
    raise NotImplementedError("Product validation has not been implemented.")


def validate_all(staging_dir: Path, validated_dir: Path) -> dict[str, Path]:
    """Validate all staged files and return the validated paths by entity."""
    # TODO: Create the output directory, validate each entity, and report invalid rows.
    raise NotImplementedError("Pipeline validation has not been implemented.")
