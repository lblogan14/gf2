from datetime import datetime
import pandas as pd
import pandas_datareader.data as web

# Specify Date Range
start = datetime(2016, 1, 1)
end = datetime.today()

# Specify symbol
symbol = 'SHA:601318'

aapl_from_google = web.DataReader("%s" % symbol, 'google', start, end)

print ("type is %s" % (type(aapl_from_google)))

# aapl_from_yahoo = web.DataReader("%s" % symbol, 'yahoo', start, end)

aapl_from_google.to_csv('%s_from_google.csv' % symbol)
# aapl_from_yahoo.to_csv('%s_from_yahoo.csv' % symbol)
