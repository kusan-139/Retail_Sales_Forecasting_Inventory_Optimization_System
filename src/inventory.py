
import numpy as np
from scipy.stats import norm

def inventory_policy(forecast, resid_std, on_hand, lead_time, service_level=0.95):
    z = norm.ppf(service_level)
    mu_L = forecast[:lead_time].sum()
    SS = z * resid_std * (lead_time**0.5)
    ROP = mu_L + SS
    return {"ROP": ROP, "order_qty": max(0, ROP-on_hand)}
