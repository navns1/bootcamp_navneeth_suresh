## Data Storage Layer

### Folder Structure
- `data/raw/`: Holds original, untouched data files (CSV format).
- `data/processed/`: Holds optimized, cleaned data files (Parquet format).

### Formats Used
1. **CSV (.csv)**: Used for raw data because it is easy for humans to open and read anywhere.
2. **Parquet (.parquet)**: Used for processed data because it saves space, processes faster, and remembers data types perfectly.

### Environment Control
We use a `.env` file to tell our code exactly where folders are without hardcoding paths. Our Python tools in `utils/storage.py` read these pathways to safely save and open files automatically based on their file type.
