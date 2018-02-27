import pandas_datareader.data as web
import datetime as dt


symbol = 'WIKI/AAPL'
df = web.DataReader(symbol, 'quandl', '2010-01-01', dt.date.today())
print(df['Close'])
