# Fizz Buzz
# Where a multiple of 3 becomes Fizz
# a multiple of 5 becomes Buzz
# a multiple of BOTH 3 and 5 becomes FizzBuzz
# all other numbers stay the same
number=int(input("Please state an integer: "))

for i in range(1,number + 1):
    if i % 3 == 0 and i % 5 == 0: 
        #print(f"{i} is a multiple of 3 and a multiple of 5") 
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        #print(f"{i} is a multiple of 3")
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        #print(f"{i} is a multiple of 5")
        print("Buzz")
    else:
        print(i)