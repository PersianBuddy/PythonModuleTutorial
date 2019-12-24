import re

# extract email from a text using regular expressions
sample_text = "This a sample text, mnajafi0014@gmail.comsdfw I want to extract this email from it"

email_pattern = re.compile("[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+.[com|net|org]")

extracted_email = email_pattern.search(sample_text)
# print(extracted_email)


###################################
# datetime module
# datetime.date()  --> Y, M, D
# datetime.time()  --> h, m, s, ms
# datetime.datetime()  --> Y, M, D, h, m, s, ms
import datetime
import pytz

today_date = datetime.date.today()
now_datetime = datetime.datetime.now()

# create time lap
time_delta = datetime.timedelta(days=4, hours=10)
new_datetime = now_datetime + time_delta
print(new_datetime)
print(today_date)
print(now_datetime)

# insert specific time zone using 'pytz' module
datetime_utc = datetime.datetime.now(tz=pytz.UTC)
datetime_iran = datetime_utc.astimezone(pytz.timezone('Iran'))
print(datetime_utc)
print(datetime_iran)

# iterate throw all time zones
# for tz in pytz.all_timezones:
#    print(tz)

# 'format' datetime object into specific form in string using 'strftime'
# B-> Month, d->day, Y->Year
formatted_date = datetime_iran.strftime('%d day of %B of %Y')
print(formatted_date)

# 'Parse' an string to a datetime object using 'strptime'
print(datetime.datetime.strptime(formatted_date, '%d day of %B of %Y'))

