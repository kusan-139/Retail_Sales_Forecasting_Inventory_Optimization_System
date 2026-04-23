from data_ingestion import load_data
from feature_engineering import make_features
from model_train import train
from config import DATA_PATH

def main():
    # 1. Load data
    df = load_data(DATA_PATH)

    # 2. Feature engineering per store–item
    df = (
        df.groupby(["store_id", "item_id"], group_keys=False)
          .apply(make_features)
          .reset_index(drop=True)
    )

    # 3. Select ONLY numeric ML features
    features = [
        c for c in df.columns
        if c not in ["qty_sold", "date", "store_id", "item_id"]
    ]

    # 4. Train model
    train(df, features)

if __name__ == "__main__":
    main()
