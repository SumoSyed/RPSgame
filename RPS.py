import random

ai_choice = random.randint(1, 3)

Rock = 1
Paper = 2
Scissors = 3

def round(user_choice, ai_choice):

    if ai_choice == Rock and user_choice == "r":
        return "Draw"
    elif ai_choice == Paper and user_choice == "r":
        return "You lose. Paper beats rock!"
    elif ai_choice == Scissors and user_choice == "r":
        return "You win. Rock beats scissors!"

    elif ai_choice == Rock and user_choice == "p":
        return "You win. Paper beats rock!"
    elif ai_choice == Paper and user_choice == "p":
        return "Draw."
    elif ai_choice == Scissors and user_choice == "p":
        return "You lose. Scissors beats paper!"

    elif ai_choice == Rock and user_choice == "s":
        return "You lose. Rock beats scissors!"
    elif ai_choice == Paper and user_choice == "s":
        return "You win. Scissors beats paper!"
    elif ai_choice == Scissors and user_choice == "s":
        return "Draw"


while True:
    answer = input("Would you like to play Rock, Paper, Scissors? Type yes or no -> ").lower()
    if answer == 'yes':
        print( round(input("Pick Rock, Paper, or Scissors. Type R or P or S: ").lower(), ai_choice))
    elif answer == 'no':
        print("To play, restart the program. Press any key to exit")
        input()
        break
    else:
        print('You must type "Yes" or "No".')
