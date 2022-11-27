from random import randint

count = 0
name = input("What is your name? ")
print(f"Welcome {name}, to the Game of Chance where you get 10 goes to correctly guess the number. If you get it correct and it is an even number, you get double your bet. If it is a multiple of 10 and you get it correct, you get 3 times your money back. If it is prime and you guess correctly, you get 5 times your money. If it is below 5 and you get it correct you only get 2% of your money back as a bonus")
score = 0
money = 0

def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


while count <= 10:
    numberToGuess = randint(0, 30)
    bet = int(input("How much would you like to bet? "))
    guess = int(input("Please guess what number you think has been chosen, from 0 to 30: "))

    if guess == numberToGuess:
        print(f"You got it correct, the number was {numberToGuess}")
        if (numberToGuess % 2) == 0:
            score = score + 1
            money = money + bet * 2  # 200% of the bet back
        elif (numberToGuess % 10) == 0:
            score = score + 1
            money = money + bet * 3  # 300% of the bet back
        elif is_prime(numberToGuess) == True:
            score = score + 1
            money = money + bet * 5  # 500% of the bet back
        elif numberToGuess < 5:
            score = score + 1
            money = money + bet * 0.2  # 2% of the bet back
        else:
            score = score + 1
            money = money + bet
    else:
        print(f"Incorrect guess, you chose {guess}, the number was {numberToGuess}")
    count = count + 1
file=open(f"users/{name}.txt", "x")
file.write(f"Name: {name.capitalize()} \nScore: {score} \nMoney Gained: £{money}")
file.close()