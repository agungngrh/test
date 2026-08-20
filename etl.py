import pandas as pd

def extract_data(source: str) -> pd.DataFrame:
    return pd.read_csv(source)