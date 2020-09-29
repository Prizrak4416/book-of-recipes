import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('../data/sf_pe_salaries_2011.csv')
# data = data.reindex(data['Id'])
data = data.drop("Id", 1)
data['BasePay'] = data['BasePay'].replace('Not Provided', '0')
data = data.fillna('0')
data['BasePay'] = data['BasePay'].astype(float)
print(data.iloc[0]['BasePay'])

# Xaxis = data.index
# XaxisPersotile = data.index / data.index.max() * 100
# Yaxis = data['BasePay'].values
# YaxisSort = sorted(Yaxis)
#
# plt.scatter(XaxisPersotile, YaxisSort)
# plt.grid()
# plt.show()

BasePay = data['BasePay'].values
BasePay = BasePay[BasePay > 1000]

step = 20000
buckets = list(range(1000, int(BasePay.max()), step))
chelikovBuckets = []
for bucketsStart in buckets:
    bucketsEnd = bucketsStart + step
    kol_vo = BasePay[(BasePay > bucketsStart) & (BasePay < bucketsEnd)]
    chelikovBuckets.append(len(kol_vo))

Xaxis = buckets
Yaxis = chelikovBuckets

plt.scatter(Xaxis, Yaxis)
plt.grid()
plt.show()