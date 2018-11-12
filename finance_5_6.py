# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# module 5
import bs4 as bs
import os
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import pickle
import requests
def save_sp500_tickers():
    resp=requests.get("https://en.wikipedia.org/wiki/list_of_S%26P_500_companies")
    soup=bs.BeautifulSoup(resp.text, "lxml")
    table=soup.find("table",{"class":"wikitable sortable"})
    tickers=[]
    for row in table.findAll("tr") [1:]:
        ticker=row.findAll("td") [0].text
        tickers.append(ticker)        
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers, f)
    print(tickers)    
    return tickers
#save_sp500_tickers()

# module 6
#crearing new function get data from yahoo
    
def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers=save_sp500_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers=pickle.load(f)
            
            if not os.path.exists("stock_dfs"):
                os.makedirs("stock_dfs")
                
                start=dt.datetime(2010,1,1)
                end=dt.datetime.now()
                
                for ticker in tickers[:100]:
                    print(ticker)
                    if not os.path.exists("stock_dfs/{}.csv".format(ticker)):
                        df=web.DataReader(ticker,"yahoo",start,end)
                        df.to_csv("stock_dfs/{}.csv".format(ticker))
                        
                    else:
                        print("Already have {}".format(ticker))
                        get_data_from_yahoo()
                
                
                
                
