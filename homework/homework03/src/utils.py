import pandas as pd


def get_summary_stats(df: pd.DataFrame, group_col: str = None) -> pd.DataFrame:
    """
    Return summary statistics for all numeric columns in a DataFrame.

    If group_col is provided, statistics are computed per group
    (e.g. per category) instead of across the whole dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset to summarize.
    group_col : str, optional
        Column name to group by before summarizing.

    Returns
    -------
    pd.DataFrame
        Summary statistics (count, mean, std, min, max, etc.)
    """
    numeric_df = df.select_dtypes(include="number")

    if group_col is not None:
        return df.groupby(group_col)[numeric_df.columns].describe()

    return numeric_df.describe()


def loop_vs_vectorized_demo(arr):
    """
    Compare elementwise squaring of an array using a Python loop
    versus a vectorized NumPy operation. Returns both results and
    confirms they match.

    Parameters
    ----------
    arr : np.ndarray

    Returns
    -------
    tuple(np.ndarray, np.ndarray, bool)
        (loop_result, vectorized_result, results_match)
    """
    import numpy as np

    loop_result = np.empty_like(arr, dtype=float)
    for i in range(len(arr)):
        loop_result[i] = arr[i] ** 2

    vectorized_result = arr ** 2

    results_match = np.allclose(loop_result, vectorized_result)
    return loop_result, vectorized_result, results_match
