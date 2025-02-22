from datetime import date, datetime, timedelta

# 1
now = date.today()
five_days_ago = now - timedelta(days=5)
print("Five days ago:", five_days_ago)

# 2
yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", now)
print("Tomorrow:", tomorrow)

# 3
dt_now = datetime.now()
dt_no_microseconds = dt_now.replace(microsecond=0)
print("Current datetime without microseconds:", dt_no_microseconds)

# 4
dt1 = datetime(2023, 2, 1, 12, 0, 0)
dt2 = datetime(2023, 2, 2, 13, 30, 0)
difference_seconds = (dt2 - dt1).total_seconds()
print("Difference in seconds:", difference_seconds)
