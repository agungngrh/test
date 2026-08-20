import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def extract_data(source, delimiter=","):
    return pd.read_csv(source, delimiter=delimiter, chunksize=1000)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def load(df: pd.DataFrame, destination: str):
    return df.to_csv(destination, index=False)


def validation(df: pd.DataFrame, requiered_columns: str) -> None:
    missing = set(requiered_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Kolom hilang: {missing}")
