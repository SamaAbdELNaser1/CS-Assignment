#CS112_A1_T2_1_20230176.py
#Author: Sama Abd El_Naser Osman Abed
# ID: 20230176
"""
purpose:game1 . the goale is to reach the number 100..How can that be ?
Each player adds a number from 1 to 10
and whoever hits the target by reaching 100 is the winner
"""
def game1():
    # set  sum and valid numbers
    sum = 0
    current_player = 1
    valid_num = range(1, 11)# Numbers that players can chose
    # welcome message
    print("Welcome to game 1")
    # Game program
    # Loop until someone reaches 100 exactly
    while sum < 100 or sum >100 :
        try:
            add = int(input(f"Player {current_player}: Add a number from 1 to {len(valid_num)} : "))
            if add in valid_num:
                sum += add
                print(f"We reached to {sum}")# Print the current sum
            else:
                print(f"Invalid number. Please enter a number from 1 to {len(valid_num)}.")
                continue
            if sum == 100:
                print(f"Player {current_player} is the winner!!!")
                break
            # If the sum bigger than 100
            elif sum > 100:
                sum-=add   # Undo the last addition
                valid_num=range(1,101-sum)  #Re_evaluation the valid numbers
                print("Error! Sum is bigger than 100.")
                continue
            current_player = 2 if current_player == 1 else 1  # Switch player for the next turn
        except:
            print("An error occurred. Please enter a valid number.")   # Handle input errors
            continue
game1() #call the function to start