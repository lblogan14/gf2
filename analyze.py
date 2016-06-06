
import pandas as pd

d2318 = pd.read_csv('2318.clean.csv',index_col=0)
d601318 = pd.read_csv('601318.clean.csv',index_col=0 )
cnyhkd = pd.read_csv('cnyhkd_rate.clean.csv',index_col=0)

# print (d601318)
print (d2318)