from datetime import datetime

date = datetime(2020, 11, 4, 14, 53)

print(date.strftime("%Y/%m/%d %H:%M:%S"))
print(date.strftime("%y/%B/%d %H:%M:%S %p"))
print(date.strftime("%a, %Y %b %d"))
print(date.strftime("%A, %Y %B %d"))
print(date.strftime("Weekday: %w"))
print(date.strftime("Day of the year: %j"))
print(date.strftime("Week number of the year: %W"))
