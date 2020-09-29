import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def loadPrices(fileName):
    dat = pd.read_csv(fileName)
    dat = dat.set_index(pd.DatetimeIndex(dat['Date']))
    dat = dat.drop('Date', 1)
    return dat


def normalizeValues(table, newColumn, existingColum):
    priceAtT0 = table.iloc[-1][existingColum]
    table[newColumn] = table.apply(lambda row: (row[existingColum] / priceAtT0), axis=1)
    return table


oil = loadPrices('../data/oilPrices.csv')
usdPrice = loadPrices('../data/usdPrices.csv')
# usdPrice = loadPrices('../data/USDRUB3.csv')


# reindex index USD = index oil
comonIndex = oil.index
usdPrice = usdPrice.reindex(comonIndex)
usdPrice = usdPrice.fillna(method='backfill')

usdPrice = normalizeValues(usdPrice, 'normalizeValues', "Price")
oilPrice = normalizeValues(oil, 'normalizeValues', "Price")

Xaxis = comonIndex
# # Y = price
oilYaxis = oil['normalizeValues'].values
usdYaxis = usdPrice['normalizeValues'].values

plt.plot(Xaxis, oilYaxis, color='blue', label='Oil Price')
plt.plot(Xaxis, usdYaxis, '--', color='red', label='usd Price')
plt.legend()
plt.show()
