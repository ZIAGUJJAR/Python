# Muhammad Zia Ur Rehman

import calendar

year = int(input("Please enter year to get matrix form for that year: "))

for i in range(1,12):
  print(calendar.monthcalendar(year,i), end="") #to remove the problem of new line just add end=""

