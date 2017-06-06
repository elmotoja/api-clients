import requests # http://docs.python-requests.org/en/latest/
import helper_functions as h
from datetime import datetime, timedelta

# TODO: add log-files to gitignore 

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
error_log = open('log-files/error_log.txt', 'w')
results_log = open('log-files/results_log.txt', 'w')
results_json = open('log-files/results_json.json', 'w')

for code in CURRENCY_CODES:
    for interval in intervals:
        date_from_s = interval[0].strftime("%Y-%m-%d")
        date_to_s = interval[1].strftime("%Y-%m-%d")
        try:
            url = 'http://api.nbp.pl/api/exchangerates/rates/' + TABELE[0] + '/'+ code + '/' + date_from_s + '/' + date_to_s + '/'
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            # log error to file
            print('error:', r.status_code, 'for code', code, file=error_log)
        else:
            result = r.json()
            success = True
    if success:
        # save the result in the 'log-files' folder
        print("success for code:", code, file=results_log)
        print(result, file=results_log)
        print(result, file=results_json)
        break
