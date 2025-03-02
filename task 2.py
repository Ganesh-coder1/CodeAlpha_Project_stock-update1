import requests
api_key ='792d42ecc5a74bd1a8593b8adf04be6a'

import pandas as pd


ticker ="EUR/USD"
interval ='1day'
api_url =f'https://api.twelvedata.com/time_series?symbol={ticker}&start_date=2025-03-02&end_date=2025_03_03&interval{interval}&outputsize=12&apikey={api_key}'
data = requests.get(api_url).json()

import pandas as pd 

ticker ="MSFT"
interval ='1day'
api_url =f'https://api.twelvedata.com/time_series?symbol={ticker}&interval={interval}&outputsize=12&apikey={api_key}'
data = requests.get(api_url).json()
data1=pd.DataFrame(data['values'])

data1['high'] = pd.to_numeric(data1['high'])
data1['close'] = pd.to_numeric(data1['close'])

# Calculate the 'bought_price' as the average of 'high' and 'low'
data1['bought_price'] = (data1['high'] + data1['low']) / 2
data1['sale_price']

data1
