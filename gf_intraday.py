import requests
import datetime
import pandas as pd
import urllib

def get_intraday_data(symbol, interval_seconds=301, num_days=10):
    # Specify URL string based on function inputs.
    url_string = 'http://www.google.com/finance/getprices?q={0}'.format(symbol.upper())
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)

    # Request the text, and split by each line
    r = requests.get(url_string).text.split()

    # Split each line by a comma, starting at the 8th line
    r = [line.split(',') for line in r[7:]]

    # Save data in Pandas DataFrame
    df = pd.DataFrame(r, columns=['Datetime','Close','High','Low','Open','Volume'])

    # Convert UNIX to Datetime format
    df['Datetime'] = df['Datetime'].apply(lambda x: datetime.fromtimestamp(int(x[1:])))

    return df

def get_daily_data(symbol, start_date, end_date ):

    ''' Daily quotes from Google. Date format='yyyy-mm-dd' '''
    # url_string = 'http://www.google.com/finance/getprices?q={0}'.format(symbol.upper())
    # url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)
    # start = datetime.date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))

    #http://www.google.com/finance/historical?q=AAPL&startdate=Nov 1, 2011&enddate=Nov 30, 2011&output=csv
    start = datetime.date(2016, 2, 3)
    end = datetime.date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))

    url_string = "http://www.google.com/finance/historical?q={0}".format(symbol.upper())
    url_string += "&startdate={0}&enddate={1}&output=csv".format(
        start.strftime('%b %d, %Y'), end.strftime('%b %d, %Y'))

    csv = urllib.urlopen(url_string).readlines()
    csv.reverse()
    for bar in xrange(0,len(csv)-1):
      ds,open_,high,low,close,volume = csv[bar].rstrip().split(',')
      open_,high,low,close = [float(x) for x in [open_,high,low,close]]
      dt = datetime.datetime.strptime(ds,'%d-%b-%y')
      self.append(dt,open_,high,low,close,volume)


    # Request the text, and split by each line
    r = requests.get(url_string).text.split()

    # Split each line by a comma, starting at the 8th line
    r = [line.split(',') for line in r[7:]]

    # Save data in Pandas DataFrame
    df = pd.DataFrame(r, columns=['Datetime','Close','High','Low','Open','Volume'])

    # Convert UNIX to Datetime format
    df['Datetime'] = df['Datetime'].apply(lambda x: datetime.fromtimestamp(int(x[1:])))

    return df


# df = get_intraday_data(symbol = 'HKG:2318', interval_seconds=301, num_days=5)
# df = get_daily_data(symbol = 'QIHU', start_date='2015-01-01', end_date='2015-06-01')

df =[]

for i in range(0,55):
    url = 'https://www.google.com/finance/historical'
    # params = {'q': 'SHA:601318','start': str(i * 30), 'num': '30', 'startdate':'01 Jan, 2009'}
    params = {'q': 'HKG:2318', 'start': str(i * 30), 'num': '30', 'startdate': '01 Jan, 2009'}

    r = requests.get(url=url, params=params)
    f= pd.read_html(r.content)[2]
    df.append(f)
    print("************* %d **********************" %i)
    print (f)


result = pd.concat(df,ignore_index=True)
# result.to_csv('2318.csv')

print (result)