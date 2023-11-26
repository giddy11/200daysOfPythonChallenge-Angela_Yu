
#BMI = weight(kg) / height2(m2)

# 🚨 Don't change the code below 👇
weight = int(input("enter your height in m: "))
height = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(f"{height} {weight}")

bmi = round(weight / (height ** 2), 2)

print(bmi)