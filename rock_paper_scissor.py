import random

user_wins = 0
computer_wins = 0
option = ["rock","paper","scissors"]

while True:
    user_input = input("Type : Rock/Papers/Scissors or Q to quit").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue
    random_numbers = random.randint(0,2)
    computer_pick = option[random_numbers]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins+=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins+=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins+=1

    else:
        print("You Lost")
        computer_wins+=1

print("You won",user_wins,"Times")
print("Computer won",computer_wins,"Times")
