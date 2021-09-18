import random
name = input('Enter your name please:')
print(f'Welcome back {name}, lets play')
while True:
    user = input("Enter a choice (rock, paper, scissors): ")
    choices = ["rock", "paper", "scissors"]
    Enemy = random.choice(choices)
    print(f"\nYou chose {user}, Enemy chose {Enemy}.\n")

    if user == Enemy:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if Enemy == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if Enemy == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user == "scissors":
        if Enemy == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break