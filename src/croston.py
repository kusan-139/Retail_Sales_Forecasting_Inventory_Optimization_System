
import numpy as np

def croston_forecast(y, alpha=0.1, h=4):
    demand = y.values
    z = demand[demand>0]
    if len(z)==0:
        return np.zeros(h)
    return np.repeat(z.mean(), h)
