# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:10:51 2019

@author: Dell
"""
import random
print("HANGMAN LETTER GAME\n")
word_list = ['cat','ice cream','pastry','pen']
word = random.choice(word_list)
#count=len(word)
guess_words=[]
letters_used=[]
count=0
#for i in range(0,count):
while(count<15):
    guess = input("Enter a letter: ")
    if not guess:
        break
    

    if guess in letters_used:
        print("You have already used this letter")
        count=count+1
        
    
    else:
        if guess in word:
            print("Correctly guessed:")
            guess_words.append(guess)
            letters_used.append(guess)
        else:
            print("Wrong guess")
            letters_used.append(guess)
    count=count+1
print("CHANCES COMPLETE")
"".join(guess_words)
if guess_words == word:
    print("YOU WON")
else:
    print("SORRY, YOU LOST")

            
            
            
    
    