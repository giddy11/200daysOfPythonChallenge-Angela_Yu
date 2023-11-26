print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
numOfPerson = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

percentage /= 100
totalBillPercentage = totalBill * percentage
profit = totalBill + totalBillPercentage
splittedProfit = round(profit / numOfPerson, 2) #this gives 33.6
# splittedProfit = "{:.2f}".format((profit / numOfPerson)) # this gives 33.60

print(f"Each person should pay: {splittedProfit}") 