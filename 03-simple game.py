###########################
# PART 10: Simple Game ###
# --- CODEBREAKER --- ###
# --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
import random


def get_guess():
    guess = list(input("enter 3 digits number"))
    while len(guess) != 3:
        print("your input is not 3 digits")
        guess = list(input("enter 3 digits number"))

    else:
        return guess


def generate_rand():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def clues(gues, rand):
    clue = []
    if gues == rand:
        return "CODE CRACKED"
    for i, num in enumerate(gues):
        if num == rand[i]:
            clue.append("Match")
        elif num in rand:
            clue.append("close")
    if clue == []:
        return ["Nope"]
    else:
        return clue


print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

seccode = generate_rand()
print(seccode)
print("code generated please guess 3 digits")
clue_report = []

while clue_report != "CODE CRACKED":
    gus = get_guess()
    clue_report = clues(gus, seccode)
    print("Here is the result of your guess:")
    for clu in clue_report:
        print(clu)
