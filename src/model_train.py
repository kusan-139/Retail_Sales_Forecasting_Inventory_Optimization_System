from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train(df, features):
    X, y = df[features], df["qty_sold"]

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=13,
        n_jobs=1
    )
    model.fit(X, y)

    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/retail_forecast_model.pkl")
