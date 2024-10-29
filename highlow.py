import random

def high_low_game(rounds):
    player_score = 0
    
    for round_number in range(1, rounds + 1):
        
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"\nRound {round_number}:")
        print(f"Your number is: {player_number}")
        print("Is your number higher or lower than the computer's number? (type 'higher' or 'lower')")

        player_guess = input("Your guess: ").strip().lower()

        
        if (player_guess == 'higher' and player_number > computer_number) or \
           (player_guess == 'lower' and player_number < computer_number):
            print(f"Correct! The computer's number was: {computer_number}")
            player_score += 1
        else:
            print(f"Wrong! The computer's number was: {computer_number}")

    print(f"\nGame Over! Your final score is: {player_score} out of {rounds}")


rounds_to_play = 5
high_low_game(rounds_to_play)
