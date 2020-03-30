import random
import sys
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def greeting():
    print("\n")
    print("Welcome to Hangman!")
    print("\n")
    print("You will need to fill in the letters for the following blank word: " + display_word)
    print("\n")
    print("The dashes represent letters - count them - that is the number of letters in this word!")
    print("\n")
    print("You are allowed 7 Mistake - and only 7 mistakes - or you will be totally and completely DEAD! Be CAREFUL!")



words = [
    "basketball",
    "fighting",
    "baseball",
    "refrigerator",
    "city",
    "bus",
    "building",
    "apple",
    "virus",
    "crisis",
]

deadman = [' =========', 
  ' +---+',
  ' |   |',
  ' O   |',
 '/|\  |',
 '/ \  |',
 '     |'
' =========']

mistakes = 0
correct = ""
secret_word = words[random.randint(0,len(words) -1)]
display_word = "_" * len(secret_word)
the_hanging = ""
letter_holder = ["_"] * len(secret_word)

greeting()

while mistakes < 7:
    
    guess = input("\nPlease guess a letter here ( all letter are lowercase):  ")
    list_word = list(secret_word)
    clear()
    if guess in secret_word:
        print("Good job. You can live a little longer!")
        for i, x in enumerate(list_word):
            if x == guess:
                letter_holder[i] = guess

        print(correct.join(letter_holder))

        if correct.join(letter_holder) == secret_word:
            print("You saved your neck! Good work!")
            break
        
    else:
        print("Nope. Sorry. Not part of secret word.")
        mistakes += 1
        the_hanging += deadman[mistakes - 1] + "\n"
        print(the_hanging)
        if mistakes == 7:
            print("\n")
            print("That was 7!")
            print("The secret word was " + "-- " + secret_word)
            print("You will soon turn and become a Walker! Part of The Walking Dead! See ya next time, DEAD PERSON . . . ")
            break




