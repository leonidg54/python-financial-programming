# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use("ggplot")
start=dt.datetime(2018,1,1)
end=dt.datetime(2018,10,4)
df=web.DataReader("TSLA","yahoo", start, end)
print(df.head(15))
df.to_csv("TSLA.csv")
df=pd.read_csv("TSLA.csv",parse_dates=True,index_col=0)
df.plot()
plt.show()
df["Adj Close"].plot()
plt.show()
df["50ma"]=df["Adj Close"].rolling(window=50,min_periods=0).mean()
print(df.head())
ax1=plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2=plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.plot(df.index, df["Adj Close"])
ax1.plot(df.index, df["50ma"])
ax2.bar(df.index, df["Volume"])
plt.show()
import bs4 as bs
import pickle
import requests
def save_sp500_tickers():
    resp=requests.get("https://en.wikipedia.org/wiki/list_of_S%26P_500_companies")
    soup=bs.BeautifulSoup(resp.txt)
    table=soup.find("table",{"class":"wikitable sortable"})
    tickers=[]
    for row in table.findAll("tr") [1:]:
        ticker=row.findAll("tr") [0].text
        tickers.append(ticker)        
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        print(tickers)    
        return tickers
save_sp500_tickers()

