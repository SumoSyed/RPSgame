import random

def ai_choice():
    return random.randint(1, 3)

Rock = 1
Paper = 2
Scissors = 3
counter = 0

def round(user_selection, ai_selection):
    ai_selection = ai_choice()
    if ai_selection == Rock and user_selection == "r":
        return "Draw"
    elif ai_selection == Paper and user_selection == "r":
        return "You lose. Paper beats rock!"
    elif ai_selection == Scissors and user_selection == "r":
        return "You win. Rock beats scissors!"

    elif ai_selection == Rock and user_selection == "p":
        return "You win. Paper beats rock!"
    elif ai_selection == Paper and user_selection == "p":
        return "Draw."
    elif ai_selection == Scissors and user_selection == "p":
        return "You lose. Scissors beats paper!"

    elif ai_selection == Rock and user_selection == "s":
        return "You lose. Rock beats scissors!"
    elif ai_selection == Paper and user_selection == "s":
        return "You win. Scissors beats paper!"
    elif ai_selection == Scissors and user_selection == "s":
        return "Draw"


while True:
    answer = input("Would you like to play Rock, Paper, Scissors? Type yes or no -> ").lower()
    counter = 0
    if answer == 'yes':
        while counter < 5:
            print( round(input("Pick Rock, Paper, or Scissors. Type R or P or S: ").lower(), ai_choice))
            counter = counter + 1
    elif answer == 'no':
        print("To play, restart the program. Press any key to exit")
        input()
        break
    else:
        print('You must type "Yes" or "No".')
