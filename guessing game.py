import random

mystery_number = random.randint(0, 99)

print("I've picked a secret number between 0 and 99. Can you guess it?")


while True:
    
    player_guess = int(input("Enter your guess: "))
    
    
    if player_guess > mystery_number:
        print("Oops! Your guess is too high.")
    elif player_guess < mystery_number:
        print("Hmm! Your guess is too low.")
    else:
        print("Congratulations! You guessed it! The number was:", mystery_number)
        break  
