
import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=["date"], dayfirst=True)
    if "stockout_flag" in df.columns:
        df = df[df["stockout_flag"]==0]
    return df
