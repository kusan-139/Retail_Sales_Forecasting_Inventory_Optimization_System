
def make_features(df):
    df = df.sort_values("date")
    # Calendar Features
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
    df["month"] = df["date"].dt.month

    for L in (1,7,14):
        df[f"lag_{L}"] = df["qty_sold"].shift(L)
    for W in (7,14,28):
        df[f"rollmean_{W}"] = df["qty_sold"].shift(1).rolling(W).mean()
        df[f"rollstd_{W}"] = df["qty_sold"].shift(1).rolling(W).std()
    return df.dropna()
