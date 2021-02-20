from functions import getWeightedFloatingAvg
from classes import SuperQueue

from twelvedata import TDClient

# Initialize client - apikey parameter is requiered
td = TDClient(apikey="YOUR_API_KEY")

# Construct the necessary time serie
ts = td.time_series(symbol="INTC", interval="1h", outputsize=100, timezone="Europe/Rome", order="asc")
ts = ts.with_bbands(ma_type="EMA").with_plus_di().with_wma(time_period=20).with_wma(time_period=40).as_pandas()

# Returns pandas.DataFrame
#data = ts.as_pandas()

ts.to_csv("data.csv", index=True)