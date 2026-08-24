import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def write_df(df: pd.DataFrame, file_path: str):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == '.csv':
        df.to_csv(path, index=False)
        print(f"Saved CSV: {path}")
    elif path.suffix == '.parquet':
        try:
            df.to_parquet(path, engine='pyarrow')
            print(f"Saved Parquet: {path}")
        except ImportError:
            print("Missing pyarrow")
    else:
        print("Format not supported")

def read_df(file_path: str) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    if path.suffix == '.csv':
        return pd.read_csv(path)
    elif path.suffix == '.parquet':
        try:
            return pd.read_parquet(path, engine='pyarrow')
        except ImportError:
            raise ImportError("Missing pyarrow")
    else:
        raise ValueError("Format not supported")
