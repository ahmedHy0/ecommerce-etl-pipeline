"""Read raw e-commerce source files and prepare them for validation."""

from pathlib import Path


def extract_customers(source_path: Path, output_path: Path) -> Path:
    """Extract customer records from a CSV file into a staging file."""
    # TODO: Read the source CSV, preserve its columns, and write the staging file.
    raise NotImplementedError("Customer extraction has not been implemented.")


def extract_orders(source_path: Path, output_path: Path) -> Path:
    """Extract order-line records from a CSV file into a staging file."""
    # TODO: Read the source CSV, preserve its columns, and write the staging file.
    raise NotImplementedError("Order extraction has not been implemented.")


def extract_products(source_path: Path, output_path: Path) -> Path:
    """Extract product records from a JSON file into a staging file."""
    # TODO: Read the source JSON and write product records in the agreed staging format.
    raise NotImplementedError("Product extraction has not been implemented.")


def extract_all(raw_dir: Path, staging_dir: Path) -> dict[str, Path]:
    """Extract all source files and return the staged file paths by entity."""
    # TODO: Create the staging directory and call each entity-specific extractor.
    raise NotImplementedError("Pipeline extraction has not been implemented.")
