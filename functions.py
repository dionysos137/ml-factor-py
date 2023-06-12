import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10,5]


def load_data():
    data = pd.read_csv("data/data_ml.csv", header=0, index_col=0)
    data["date"] = pd.to_datetime(data["date"])
    data = data[(data["date"]<"2019-01-01") & (data["date"]>"1999-12-31")]
    data.sort_values(["date","stock_id"], inplace=True)
    return data

features_short = ["Div_Yld", "Eps", "Mkt_Cap_12M_Usd", "Mom_11M_Usd", 
                    "Ocf", "Pb", "Vol1Y_Usd"]