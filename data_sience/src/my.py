import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
https://www.finam.ru/profile/cryptocurrencies/btc-usd/export/?market=520&em=484429&token=&code=BTCUSD&apply
=0&df=1&mf=8&yf=2000&from=01.09.2000&dt=27&mt=8&yt=2020&to=27.09.2020&p=8&f=BTCUSD_000901_200927&e=.csv&cn=BTCUSD&d
tf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=5&sep2=4&datf=4&at=1
'''
# def loadPrices(fileName):
#     dat = pd.read_csv(fileName)
#     p = pd.Series(dat['<TICKER> <PER> <DATE> <TIME> <CLOSE>'])
#     a, b = p.apply(lambda row: row.split()[2]), p.apply(lambda row: float(row.split()[-1]))
#     result = pd.DataFrame({'date': a, 'price': b})
#     result = result.set_index(pd.DatetimeIndex(result['date']))
#     result = result.drop('date', 1)
#     return result
#
#
# def normalizeValues(table, newColumn, existingColum):
#     priceAtT0 = table.iloc[0][existingColum]
#     table[newColumn] = table.apply(lambda row: (row[existingColum] / priceAtT0), axis=1)
#     return table
#
#
# usdPrice = loadPrices('../data/XAU.csv')
# usdPrice = normalizeValues(usdPrice, 'normalaze', 'price')
#
#
#
# Xaxis = usdPrice.index
# usdYaxis = usdPrice['normalaze'].values
# print(max(usdYaxis))
#
# plt.plot(Xaxis, usdYaxis, '--', color='red', label='usd Price')
# plt.legend()
# plt.show()


# dat = pd.read_csv('../data/USDRUB4.csv', sep=' ')
# p = pd.DataFrame(dat)

a = pd.read_csv('USDBYN2010_2020.csv', index_col=0)
print(a['price'].describe())