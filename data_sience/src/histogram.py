import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm


def loadPrices(fileName):
    dat = pd.read_csv(fileName)
    dat = dat.set_index(pd.DatetimeIndex(dat['Date']))
    dat = dat.drop('Date', 1)
    return dat


def normalizeValues(table, newColumn, existingColum):
    priceAtT0 = table.iloc[-1][existingColum]
    table[newColumn] = table.apply(lambda row: (row[existingColum] / priceAtT0), axis=1)


spx = loadPrices('../data/^spx_d.csv')
spx = spx[['Close']]
spx = spx.assign(pctChange=spx.pct_change())

close = spx['pctChange'].values[1:]
n, buckets, patches = plt.hist(close, 50)

mean = close.mean()
std = close.std()
mu = mean
sigma = std
bestFitLine = norm.pdf(buckets, mu, sigma)
plt.plot(buckets, bestFitLine, 'y--')
plt.show()
