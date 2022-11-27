number = int(input("What number would you like to find the factorial of? "))
factorial = 1
if number < 0:
    print("Number cannot be negative")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial = factorial*i
    print(f"The factorial of {number} is {factorial}")
    print(f"{number}! is {factorial}")
