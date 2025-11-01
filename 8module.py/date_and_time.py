from datetime import datetime, date, time, timedelta

# print(datetime.now())           #Returns current local datetime

# print(datetime.today())

# a=datetime.strptime("2025-07-26", "%Y-%m-%d")           # convert string to date time
# print(type(a))


# now  = datetime.now()
# b= now.strftime("%d-%m-%Y %H:%M:%S")                # convert  date time to string
# print(b)
# print(type(b))


# print(datetime(2025, 7, 26, 10, 45))            # Creates a datetime object


# print(date.today())             # Returns today's date only


# print(date(2020,5,6))                  # Creates a date object

# print(time(12,2,3))                     # create a time object

# now = datetime.now()
# tomorrow = now+timedelta(days=1)
# yesterday = now -timedelta(days=1)
# print(tomorrow)
# print(yesterday)