import requests # http://docs.python-requests.org/en/latest/
import helper_functions as h
from datetime import datetime, timedelta

# r = requests.get("http://api.nbp.pl/api/exchangerates/tables/A")

TABELE = ['a', 'b']
CURRENCY_CODES = h.import_country_codes('ISO4217_codes.csv')
print(CURRENCY_CODES)
# date_from = "2012-01-01"
# date_to = "2012-01-31"
date_to = datetime.now()
date_from = date_to - timedelta(days = 180)
intervals = h.divide_interval_into_smaller_pieces(date_from, date_to)

for interval in intervals:
    date_from_s = interval[0].strftime("%Y-%m-%d")
    date_to_s = interval[1].strftime("%Y-%m-%d")
    url = 'http://api.nbp.pl/api/exchangerates/rates/' + TABELE[0] + '/'+ CURRENCY_CODES[0] + '/' + date_from_s + '/' + date_to_s + '/'
    print(url)
    # r = requests.get(url)
    # result = r.json()
    # print(result)

# save the result in the 'results' folder