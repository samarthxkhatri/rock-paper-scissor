import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices


def check_win(player, computer):
    print("You chose " + player + " and computer chose " + computer)

    if player == computer:
        return "It is a tie"

    elif player == "rock":
        if computer == "scissors":
            return "Player wins"
        else:
            return "Computer wins"

    elif player == "scissors":
        if computer == "rock":
            return "Computer wins"
        else:
            return "Player wins"

    elif player == "paper":
        if computer == "rock":
            return "Player wins"
        else:
            return "Computer wins"


choices = get_choices()
print(check_win(choices["player"], choices["computer"]))