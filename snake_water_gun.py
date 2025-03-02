import random

def rules(rows, cols, rules):
    print("\nRules (D=Draw, W=Win, L=Lose) and (C=Computer, P=Player):\n")
    for i in range(rows):
        row = []
        for j in range(cols):
            if j == 0:
                row.append("->" if i == 0 else "C.Snake" if i == 1 else "C.Water" if i == 2 else "C.Gun  ")
            elif j == 1:
                row.append("    P.Snake" if i == 0 else "    D" if i == 1 else "    W" if i == 2 else "    L")
            elif j == 2:
                row.append("    P.Water" if i == 0 else "        L" if i == 1 else "        D" if i == 2 else "        W")
            else:
                row.append("    P.Gun  " if i == 0 else "        W" if i == 1 else "        L" if i == 2 else "        D")
        rules_matrix.append(row)

    for row in rules_matrix:
        for col in row:
            print(col, end=" ")
        print("\n")


def snake_water_gun(my_score, computer_score):
    print("\nLets Play!")
    print("You are the Player and the Computer is the Opponent.")
    print("You have to choose between Snake, Water, and Gun.")
    print("\nPress 1 for Snake\nPress 2 for Water\nPress 3 for Gun")
    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3"]:
        choices = {"1": "Snake", "2": "Water", "3": "Gun"}
        player_choice = choices[choice]
        computer_choice = random.choice(["Snake", "Water", "Gun"])
        
        print(f"\nYou chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a Draw!!")
        elif (player_choice == "Snake" and computer_choice == "Water") or \
             (player_choice == "Water" and computer_choice == "Gun") or \
             (player_choice == "Gun" and computer_choice == "Snake"):
            print("You Win!!")
            my_score += 1
        else:
            print("Computer Wins!!")
            computer_score += 1

        print(f"\nYour Score: {my_score}")
        print(f"Computer Score: {computer_score}")

        play_again(my_score, computer_score)
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        snake_water_gun(my_score, computer_score)

def play_again(my_score, computer_score):
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        snake_water_gun(my_score, computer_score)
    else:
        print("\nThanks for playing!!")
        print(f"Final Score -> You: {my_score} | Computer: {computer_score}")

my_score, computer_score = 0, 0
rows, cols = 4, 4
rules_matrix = []
title = "SNAKE WATER GUN!!"
print(title.center(100))
rules(rows, cols, rules_matrix)
snake_water_gun(my_score, computer_score)
