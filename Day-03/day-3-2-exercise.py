# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Your bmi is 27, you are slightly overweight.

bmh_result = int(weight / (height ** 2))
print(bmh_result)

if (bmh_result < 18.5):
    print(f"Your BMI is {bmh_result}, you are underweight.")
elif (bmh_result < 25):
    print(f"Your BMI is {bmh_result}, you have a normal weight.")
elif (bmh_result < 30):
    print(f"Your BMI is {bmh_result}, you are slightly overweight.")
elif (bmh_result < 35):
    print(f"Your BMI is {bmh_result}, you are obese.")
else:
    print(f"Your BMI is {bmh_result}, you are clinically obese.")