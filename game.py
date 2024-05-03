import random
number = random.randint(1, 10)
player_name = input("Hello Dude, what is your name?")
number_of_guesses = 0
print("Okay " + player_name + " Guess a number between 1 and 10")
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    elif guess == number:
        break
if guess == number:
    print("You guessed the number in " + str(number_of_guesses) + " tries!")
else:
    print("You did not guess the number. The number was " + str(number))