import pandas as pd
import numpy as np

def add_derived(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["price_per_sqm"] = df["price"] / (df["sqft_living"] / 10.764)
    df["modern"] = (df["yr_built"] >= 2000) | (df["yr_renovated"] >= 2000)
    return df


def compute_stats(df: pd.DataFrame) -> dict:
    stats = {
        "count": len(df),
        "price_mean": round(df["price"].mean(), 2),
        "price_median": round(df["price"].median(), 2),
        "price_min": float(df["price"].min()),
        "price_max": float(df["price"].max()),
        "avg_price_per_sqm": round(df["price_per_sqm"].mean(), 2),
        "modern_pct": round(df["modern"].mean() * 100, 2),
    }
    stats["price_by_zip"] = df.groupby("zipcode")["price"].mean().round(2).head(10).to_dict()
    stats["price_by_bedrooms"] = df.groupby("bedrooms")["price"].mean().round(2).to_dict()
    stats["price_by_waterfront"] = df.groupby("waterfront")["price"].mean().round(2).to_dict()
    stats["cond_by_grade"] = df.groupby("grade")["condition"].mean().round(2).to_dict()
    return stats
