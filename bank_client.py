import requests # http://docs.python-requests.org/en/latest/
import helper_functions as h
from datetime import datetime, timedelta

TABELE = ['a', 'b']
CURRENCY_CODES = h.import_country_codes('ISO4217_codes.csv')
# print(CURRENCY_CODES)
# CURRENCY_CODES = ['gbr', 'pln']
# date_from = "2012-01-01"
# date_to = "2012-01-31"
date_to = datetime.now()
date_from = date_to - timedelta(days = 180)
intervals = h.divide_interval_into_smaller_pieces(date_from, date_to)

success = False

for code in CURRENCY_CODES:
    for interval in intervals:
        date_from_s = interval[0].strftime("%Y-%m-%d")
        date_to_s = interval[1].strftime("%Y-%m-%d")
        try:
            url = 'http://api.nbp.pl/api/exchangerates/rates/' + TABELE[0] + '/'+ code + '/' + date_from_s + '/' + date_to_s + '/'
            # print(url)
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            # TODO: log error to file
            print('error:', r.status_code, 'for code', code)
        else:
            result = r.json()
            print(result)
            success = True
    if success:
        print("success for code:", code)
        break

# save the result in the 'results' folder