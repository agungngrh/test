import pandas as pd
from etl import transform, validation


def test_transform_data_drops_na():
    df = pd.DataFrame({"a": [1, None, 3]})
    result = transform(df)
    assert result.isnull().sum().sum() == 0


def test_validate_schema_raises_on_missing_column():
    df = pd.DataFrame({"a": [1, 2, 3]})
    try:
        validation(df, required_columns=["a", "b"])
        assert False, "Harusnya raise ValueError"
    except ValueError:
        pass
