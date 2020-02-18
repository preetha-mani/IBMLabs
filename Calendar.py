import calendar

y=int(input("Enter Year:"))
m=int(input("Enter Month:"))
print("The Current Calendar:",calendar.month(y,m))
print("The Calendar:",calendar.calendar(y))
print("Leap Year or not:",calendar.isleap(y))