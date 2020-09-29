import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import calendar
import time

" USD Cur_ID = 145 ondate=2016-7-01"
"https://www.nbrb.by/api/exrates/rates/145?ondate=2016-7-01"

Cur_ID = 145

# load json file with nbrb.by site
def loadPrices(val, filename):
    url = 'https://www.nbrb.by/api/exrates/rates/{}?ondate={}'.format(val, filename)
    while True:
        try:
            dat = requests.get(url, timeout=5)
            break
        except:
            time.sleep(3)
    dat = dat.json()
    return dat

# make list calendar
def makeCalendar(last_date):
    dates = []
    c = calendar.Calendar(0)
    for i in range(2010, 2021):
        for j in range(1, 13):
            for weeks in c.monthdayscalendar(i, j):
                for day in weeks:
                    if day != 0:
                        dates.append('{}-{}-{}'.format(i, j, day))
                    if len(dates) != 0:
                        if dates[-1] == last_date:
                            return dates
    return dates


def make_table(calMas):
    table = pd.DataFrame(columns=['date', 'price'])
    for i in range(len(calMas)):
        a = loadPrices(Cur_ID, calMas[i])
        if a['Cur_OfficialRate'] > 100:
            table.loc[i] = [calMas[i], a['Cur_OfficialRate'] / 10000]
        else:
            table.loc[i] = [calMas[i], a['Cur_OfficialRate']]
        print(calMas[i])
    table = table.set_index(pd.DatetimeIndex(table['date']))
    table = table.drop('date', 1)
    return table


# url = loadPrices('https://www.nbrb.by/api/exrates/currencies')
# for i in url:
#     if i['Cur_Abbreviation'] == 'USD':
#         print(i['Cur_ID'])


calendar_mas = makeCalendar('2020-9-28')
table_price = make_table(calendar_mas)
print(table_price)
table_price.to_csv('1.csv')


