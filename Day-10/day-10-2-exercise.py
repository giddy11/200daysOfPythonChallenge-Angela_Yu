def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return 1
        print("Leap year")
      else:
        return 0
        print("Not leap year")
    else:
        return 1
        print("Leap year")
  else:
        return 0
        print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if (is_leap(year) == 1 and month == 2):
    #  month_days[2] += 1
     return 29
  else:
     return month_days[month - 1] 
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a month: ")) # Enter a month
days = days_in_month(year, month)
print(days)

