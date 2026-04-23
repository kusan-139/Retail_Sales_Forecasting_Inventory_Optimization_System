
from fastapi import FastAPI
import numpy as np
from src.inventory import inventory_policy

app = FastAPI()

@app.post("/replenishment")
def recommend(on_hand:int, lead_time:int):
    forecast = np.random.poisson(5,30)
    return inventory_policy(forecast, forecast.std(), on_hand, lead_time)
