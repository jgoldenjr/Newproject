
#secret word the player is guessing
secretWord = "Jimmie"
lettersGuessed = ""

#number of turns before a loss
failureCount = 6

#loop until player has too many attempts
#break loop if success
while failureCount > 0:

    #Get the guessed letter from player
    guess = input("Enter a letter: ")

    if guess in secretWord:
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Incorrect. There are no {guess} in the secret word. {failureCount} turn(s) left.")

    #maintain a list of all letters guessed
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    #If there were no wrong letters, then the player won
    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secretWord}. You won!")
        break 

else:
    print("Sorry you didnt win. If at first you dont succeed try, try again!")