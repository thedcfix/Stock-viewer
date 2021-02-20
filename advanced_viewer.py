from functions import getWeightedFloatingAvg, getAvg, getMaxes, getMins
from classes import SuperQueue, TuplesContainer

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from pylab import *

#reading data from .csv
data = pd.read_csv("data.csv")
stock = data["close"].values
volume = data["volume"].values

upper_band = data["wma1"].values
lower_band = data["wma2"].values

# calculating the average volume. Increasing the average multiplier can filter the most significant values (e.g. 1.2x)
multiplier = 1.5
average = getAvg(volume)
average *= multiplier

res = [i for i,v in enumerate(volume) if v > average]

# printing stock and volume
fig = plt.figure("Trend analysis")
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(stock, 'k', color="red", label="Stock")
ax1.plot(upper_band, 'k', color="grey", label="Upper")
ax1.plot(lower_band, 'k', color="purple", label="Lower")
ax1.legend(framealpha=0.5)
ax2.plot(volume, 's', color="orange", label="Volume")
ax2.axhline(y=average, color="purple", linestyle='-', label=str("Average " + str(multiplier) + "x"))
ax2.legend(framealpha=0.5)

# connecting volume and stock value
for i in res:
    xy = (i,volume[i])
    xy2 = (i,stock[i])
    con = ConnectionPatch(xyA=xy, xyB=xy2, coordsA="data", coordsB="data", axesA=ax2, axesB=ax1, color="grey", linestyle="dotted")
    ax2.add_artist(con)

# drawing max and min
max = getMaxes(stock)
min = getMins(stock)

x_max = max.get_x()
y_max = max.get_y()

x_min = min.get_x()
y_min = min.get_y()

ax1.plot(x_max, y_max, '--',color="green", label="Max")
ax1.plot(x_min, y_min, '--',color="blue", label="Min")
ax1.legend(framealpha=0.5)

#plotting results
plt.show()