import csv
import dateutil # https://dateutil.readthedocs.io/en/stable/
from dateutil.parser import *
from datetime import datetime, timedelta

def import_country_codes(file):
    codes_list = []
    with open(file, newline='') as f:
        for line in csv.DictReader(f):
            codes_list.append(line['Alphabetic Code'])
    return codes_list


def divide_interval_into_smaller_pieces(date_from, date_to, number_of_days_in_interval = 90):
    intervals = []
    now = date_from

    while now < date_to:
        interval = [now, now + timedelta(days = number_of_days_in_interval)]
        intervals.append(interval)
        now += timedelta(days = number_of_days_in_interval)

    return intervals


# # test
# date_to = datetime.now()
# date_from = date_to - timedelta(days = 180)
# intervals = divide_interval_into_smaller_pieces(date_from, date_to)

# for interval in intervals:
#     print(interval[0])
#     print(interval[1])
#     print('----')
