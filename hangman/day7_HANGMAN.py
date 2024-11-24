#HANGMAN 

import random

from day7_hangman_words import word_list
from day7_hangman_arts import logo, stages

word = random.choice(word_list)
length = len(word)
chosen_word = length * ["_"]
attempts = 6

print(logo)
print(f"Welcome to the Hangman Game!\nYour word is: {chosen_word}")
print(stages[6])
while attempts > 0 and "_" in chosen_word:
    l1 = input("Guess a letter: ")
    if not len(l1) == 1:
        print("Please enter only one letter")
    elif l1 not in word:
        print("Incorrect guess!\n", stages[attempts -1])
        attempts -= 1
        print(f"You have {attempts} attempt!")
    else: 
        for i, letter in enumerate(word):
            if letter == l1:
                chosen_word[i] = letter
        print(" ".join(chosen_word))

if "_" not in chosen_word:
    print("\nCongratulations, you won! The word was ", word)
else:
    print(f"Attpemt is over. Your word  was {word} ")



