age = int(input("What is your current age? "))

years_left = 90 - age

days = 365 * years_left
weeks = 52 * years_left
months = 12 * years_left

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)