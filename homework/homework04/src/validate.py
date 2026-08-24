import pandas as pd


def validate_dataframe(df: pd.DataFrame, required_columns: list, name: str = "dataset") -> dict:
    """
    Run basic validation checks on a freshly ingested DataFrame.

    Checks that all required columns are present, reports the shape,
    and counts missing values per column. Does not raise on failure —
    returns a report dict so the caller can decide how to handle issues.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset to validate.
    required_columns : list
        Column names that must be present.
    name : str
        Label used in printed output, for readability when validating
        multiple datasets in the same notebook.

    Returns
    -------
    dict
        {
          "shape": (rows, cols),
          "missing_columns": [...],
          "na_counts": {col: count, ...},
          "passed": bool
        }
    """
    missing_columns = [c for c in required_columns if c not in df.columns]
    na_counts = df.isna().sum().to_dict()
    passed = len(missing_columns) == 0

    print(f"--- Validation report: {name} ---")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    if missing_columns:
        print(f"MISSING required columns: {missing_columns}")
    else:
        print("All required columns present.")
    print(f"NA counts per column: {na_counts}")
    print(f"Validation passed: {passed}")

    return {
        "shape": df.shape,
        "missing_columns": missing_columns,
        "na_counts": na_counts,
        "passed": passed,
    }
