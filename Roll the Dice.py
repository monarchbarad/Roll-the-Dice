import random

#To roll the dice.
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

#Ask user for the number of players.
while True:
    players = input("Enter the Number of players ( 2 - 4 ): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2 - 4 Players.")
    else:
        print("Invalid, Try Again.")
        
#Main Body-function.

max_score = 100
player_score = [0 for _ in range(players)]

#Roll the dice for each player.
while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer ", player_idx+1," turn just started.\n")
        current_score = 0
        print("Your Total Score is: ",current_score)

        while True:
            should_roll = input("Would you like to roll the Dice? (y or n): ")
            print("\nIf roll 1!, your score will be 0.")
            if should_roll.lower() != "y":
                break
    
            value = roll()
            if value == 1:
                print("Oops you rolled 1!, your turn is 'Done'.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your Current Score is: ",current_score)
        player_score[player_idx] += current_score
        print("Your Total Score is: ",player_score[player_idx])
        
#Telling who is the Winner.
max_score =max(player_score)
win_idx = player_score.index(max_score)
print("Player number",win_idx+1,"is the winning Score of :",max_score)