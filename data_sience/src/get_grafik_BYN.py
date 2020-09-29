import matplotlib.pyplot as plt
import pandas as pd


def loadPrices(fileName):
    dat = pd.read_csv(fileName, index_col=0)
    # dat = dat.set_index(pd.DatetimeIndex(dat['date']))
    dat.index = pd.DatetimeIndex(dat.index)
    # dat = dat.drop('date', 1)
    return dat


def normalizeValues(table, newColumn, existingColum):
    priceAtT0 = table.iloc[0][existingColum]
    table[newColumn] = table.apply(lambda row: (row[existingColum] / priceAtT0), axis=1)
    return table

usdByn = loadPrices('USDBYN2010_2020.csv')
usdByn = normalizeValues(usdByn, 'procent', 'price')

Xaxis = usdByn.index
Yaxis = usdByn['procent'].values

plt.plot(Xaxis, Yaxis)
plt.grid()
plt.show()