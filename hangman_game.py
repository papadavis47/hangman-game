import random


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

deadman = ['=========', 
  '+---+',
  '|   |',
  'O   |',
 '/|\  |',
 '/ \  |',
 '     |'
'=========']

mistakes = 0
correct = ""

secret_word = words[random.randint(0,len(words) -1)]
guess = ""
display_word = "_" * len(secret_word)
the_hanging = ""


print("Welcome to Hangman!")
print("\n")
print("You will need to fill in the letters for the following word:\n" + display_word)
print("\n")
print("You are allowed 7 Mistake - and only 7 mistakes or you will totally and completely dead! Be careful!")
print("\n")
print(secret_word)



while mistakes < 7:
    guess = input("Please guess a letter here ( all letter are lowercase):   ")
    word_holder = ["_"] * len(secret_word)
    list_word = list(secret_word)
    if guess in list_word:
        for i, x in enumerate(list_word):
            if guess == x:
                word_holder[i] = x
        print(correct.join(word_holder))
        print("Good. You can live a little longer!")
    else:
        mistakes += 1
        the_hanging += deadman[mistakes - 1] + "\n"
        print(the_hanging)

print("You are fucking dead! See ya next time, DEAD PERSON")
print(the_hanging)
