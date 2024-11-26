import random
words=["noura","mahmoud","ali"]
word=random.choice(words)
scramble="".join( random.sample(word,len(word)))
attempts=5
while attempts>0:
    print("the scramble word is :",scramble)
    guess=input("enter your guess: ")

    if guess==word:
        print ("congratulion ! this is correct word")
        break
    else:
        attempts -=1
        print(f"incorrect word ,you have {attempts} now")

if attempts==0:
    print (f"you are out of attempts. the correct word is {word}")