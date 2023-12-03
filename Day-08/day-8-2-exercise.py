#Write your code below this line 👇
def prime_checker(number):
    prime = 1
    for i in range(2, number):
        if number == 2 or number == 3:
            prime = 1
            break
        if number % (i) != 0:
            continue
        else:
            prime = 0
            break

    if prime == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



