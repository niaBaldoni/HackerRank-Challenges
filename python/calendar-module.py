import calendar

# we get the input in a single line, containing the space separated month, day and year
# date = [mm, dd, yyyy]
date = list(map(int, input().split()))
dd = date[1]
mm = date[0]
yyyy = date[2]

print((calendar.day_name)[calendar.weekday(yyyy, mm, dd)].upper())
