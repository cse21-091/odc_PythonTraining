import random

words = ["car","bike", "train"]

print("Group19")
print("Welcome to the game hangman!")

display = []
lives = 7

chosen = random.choice(words)
length = len(chosen)  #Length of the word
print("I'm thinking of a word that is {} letters long!".format(length)) #Player is hinted in the number of letters in the word

for letter in range (length):
    display += "_"  # If the player has guessed correctly, replace it
    
end_game = False   # The game has not ended and the player continues to guess 

while not end_game:  
    guess = input("Guess a letter: ").lower()  #Player is prompted to guess a letter in lower case 
    for position in range(length):
        letter = chosen[position]   
        if letter == guess:    
            display[position] = letter      
            print(display)  
    if guess not in chosen:    # The player guesses a letter that is not in the target
        lives -= 1
        print ("Oops! That letter is not in my word.")
        if lives == 0:         #The number of chances(lives) is 0 
            end_game = True    #Player has lost and the game ends
            print(f"You lose! Correct answer was {chosen}")
    if "_" not in display:
        end_game = True
        print("You win!")