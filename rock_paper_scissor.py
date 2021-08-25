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
