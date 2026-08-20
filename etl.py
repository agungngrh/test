import pandas as pd


def extract_data(source: str) -> pd.DataFrame:
    return pd.read_csv(source)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def load(df: pd.DataFrame, destination: str):
    return df.to_csv(destination, index=False)
