#Rock/Papers/Scissors

import random

def ai_choice():
    return random.randint(1, 3)

Rock = 1
Paper = 2
Scissors = 3
result = ["Draw", "You win this round.", "You lose this round."]


def round(user_selection, ai_selection):
    ai_selection = ai_choice()
    if ai_selection == Rock and user_selection == "r":
        return result[0]
    elif ai_selection == Paper and user_selection == "r":
        return result[2]
    elif ai_selection == Scissors and user_selection == "r":
        return result[1]

    elif ai_selection == Rock and user_selection == "p":
        return result[1]
    elif ai_selection == Paper and user_selection == "p":
        return result[0]
    elif ai_selection == Scissors and user_selection == "p":
        return result[2]

    elif ai_selection == Rock and user_selection == "s":
        return result[2]
    elif ai_selection == Paper and user_selection == "s":
        return result[1]
    elif ai_selection == Scissors and user_selection == "s":
        return result[0]
    if result[1]:
        player = player + 1
    elif result[2]:
        computer = computer + 1

while True:
    answer = input("Would you like to play Rock, Paper, Scissors? Type yes or no -> ").lower()
    count = 0
    player_score = 0
    computer_score = 0

    if answer == 'yes':
        while count < 10:
            game = round(input("Pick Rock, Paper, or Scissors. Type R or P or S: ").lower(), ai_choice)
            print(game)
            count = count + 1
            if game == "You win this round.":
                player_score = player_score + 1
            elif game == "You lose this round.":
                computer_score = computer_score + 1
            print("Round: " + str(count))
            print("Your score: " + str(player_score))
            print("Computer score: " + str(computer_score))

            while count == 10:
                if player_score > computer_score:
                    print("Congrats! You won the game.")
                    break
                elif player_score == computer_score:
                    print("The game was a draw.")
                    break
                elif player_score < computer_score:
                    print("Sorry. You lost this game.")
                    break
                
    elif answer == 'no':
        print("To play, restart the program. Press any key to exit")
        input()
        break
    else:
        print('You must type "Yes" or "No".')
