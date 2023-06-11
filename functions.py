import numpy as np
import pandas as pd
def load_data():
    data = pd.read_csv("data/data_ml.csv", header=0, index_col=0)
    data["date"] = pd.to_datetime(data["date"])
    data = data[(data["date"]<"2019-01-01") & (data["date"]>"1999-12-31")]
    data.sort_values(["date","stock_id"], inplace=True)
    return data