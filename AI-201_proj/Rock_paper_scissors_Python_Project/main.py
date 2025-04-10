import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

Paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#list
moves = [Rock, Paper, Scissor]

def play_game():

    #condition
    play = True

    while play:

        #computer choice
        Comp_turn_index = random.randint(0, 2)
        Comp_turn = moves[Comp_turn_index]

        #User input
        try:
            User_turn = int(input("\nType 0 for Rock, 1 for Paper and 2 for Scissor: "))
            if User_turn < 0 or User_turn > 2:
                print("\nInvalid Choice! please choose a number 0, 1 or 2")
                continue
        except ValueError:
            print("\nInvalid input! please enter a number 0, 1 or 2")
            continue

        if User_turn == 0 and Comp_turn == moves[0]:
            User_turn = Rock
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nDraw")
        elif User_turn == 0 and Comp_turn == moves[1]:
            User_turn = Rock
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou lose")
        elif User_turn == 0 and Comp_turn == moves[2]:
            User_turn = Rock
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou won")
        elif User_turn == 1 and Comp_turn == moves[0]:
            User_turn = Paper
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou won")
        elif User_turn == 1 and Comp_turn == moves[1]:
            User_turn = Paper
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nDraw")
        elif User_turn == 1 and Comp_turn == moves[2]:
            User_turn = Paper
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou lose")
        elif User_turn == 2 and Comp_turn == moves[0]:
            User_turn = Scissor
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou lose")
        elif User_turn == 2 and Comp_turn == moves[1]:
            User_turn = Scissor
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nYou won")
        elif User_turn == 2 and Comp_turn == moves[2]:
            User_turn = Scissor
            print(f"Your Choice:\n {User_turn}")
            print(f"Computers Choice:\n {Comp_turn}")
            print("\nDraw")
        else:
            print("\nNot a valid choice")

        if input("\nWant to play more? (Y/N): ").lower() != "y":
            play = False

        
#start game
play_game()