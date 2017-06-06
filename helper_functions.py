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
    # liczba_dni = 14 # (tounix(data_do) - tounix(data_do))/4000
    # liczba_okresow_90 = int(liczba_dni / 90)
    intervals = []
    # date_from = parse(date_from)
    # date_to = parse(date_to)
    now = date_from

    while now < date_to:
        interval = [now, now + timedelta(days = number_of_days_in_interval)]
        intervals.append(interval)
        now += timedelta(days = number_of_days_in_interval)

    return intervals

    # now = datetime.datetime.now()
    # print(now)
    # print(now.year)
    # print(now.hour)

    
    # liczba_dni = 14 # (tounix(data_do) - tounix(data_do))/4000
    # liczba_okresow_90 = int(liczba_dni / 90)
    # kawalki = []

    # for i in range(liczba_okresow_90):
    #     kawalek = [date_from + i*90,date_from+(i+1)*90]
    #     kawalki.append(kawalek)

    # return kawalki



# test
date_to = datetime.now()
date_from = date_to - timedelta(days = 180)
intervals = divide_interval_into_smaller_pieces(date_from, date_to)

for interval in intervals:
    print(interval[0])
    print(interval[1])
    print('----')
