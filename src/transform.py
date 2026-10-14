
import pandas as pd
def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy(); df['name_len'] = df['name'].str.len(); return df
