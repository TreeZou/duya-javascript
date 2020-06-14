# This is a guess the age game.

import random
guessTaken = 0

print("Hello! what is your name?")

myName = input()

age = random.randint(18, 30)

print("Well, " + myName + ', i am thinking of my age between 18 and 30.')

while guessTaken < 18:
    print("Take a guess.")  # There are four spaces in front of print.

    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1

    if guess < age:
        print("Your guess is to low.")  # There are eight spaces in front;

    if guess > age:
        print("Your guess is too high.")

    if guess == age:
        break

if guess == age:
    guessTaken = str(guessTaken)
    print("Good job, " + myName + ", You guessed my age in " +
          guessTaken + " guesses!")
    if guess != age:
        number = str(age)
        print("Nope. The number i was thinking of was " + age)
