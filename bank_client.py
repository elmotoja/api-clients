import requests # http://docs.python-requests.org/en/latest/

r = requests.get("http://api.nbp.pl/api/exchangerates/tables/A")

result = r.json()

print(result[0]['table'])
print(result[0]['no'])
print(result[0]['effectiveDate'])

# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.hour)

# print(datetime.datetime.utcnow())