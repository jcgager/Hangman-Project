import json
import random

#Name of the file
file_Name = 'Hangman_Words_Complex.json'
#Open and read the file
js_Data = open(file_Name, 'r')
Data = js_Data.read()

#Parse the file
js = json.loads(Data)
#Variable for the secret word
secret = ""
#Letters guessed variable
lg = "" 
#Hint about the secret word
hint = ""

#Random number chosen between 1 and 5
num = str(random.randint(1,5))
#Player chooses the word list
str = input("Choose between easy, medium or hard: ")
if str == 'hard':
    print('\n')
    print('Tip: Hard words start with a capital letter \n')

for i in js[num]:
    secret = secret + i[str]["word"]
    hint = hint + i[str]["hint"]
print('\nHint: ',hint,'\n')

#The number of turns before the player loses
FailureCount = 6

#loop until player has made too many failed attempts
#Will break loop if player succeeds instead
while FailureCount > 0:
    guess = input('Enter a letter: ')

    if guess in secret:
        print(f'Correct, there are one or more {guess} in the secret word.')
    else:
        FailureCount -= 1
        print(f'Incorrect, there are no {guess} in the secret word. {FailureCount} turn(s) left')

    #Maintain a collection of all letters guessed
    lg = lg + guess
    wlc = 0

    for letter in secret:
        if letter in lg:
            print(f"{letter}", end="")
        else:
            print('_', end="")
            wlc += 1
    print("\n")
    #If there were no wrong letters, the player won
    if wlc == 0:
        print('Congrats! You correctly guessed the word', secret, ', You won!\n')
        break
else:
    print("Sorry, you didn't win this time, Try again.\n")