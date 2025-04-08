#random num by computer
import random

#list of numbers from 1 to 100
numbers = list(range(1, 101, +1))

#random num selected each time
comp_numb = random.choice(numbers) 

#basic ui
print("""   

⠀⠀⠀⣀⣤⣶⡶⠿⢿⣿⣶⣶⣤⣀⠀⠀⠀
⠀⢀⣾⣿⠋⠁⠀⠀⠀⠀⠙⢿⣿⣿⣷⣄⠀
⠀⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⡄
⠘⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇     NUMBER GUESSING
⠀⠹⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠇        GAME 🎮 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
   
""")

def Numb_guessing_game():

    #lives
    Numb_of_tries = 5

    while Numb_of_tries > 0:
        
        #user guess managing
        User_guess = int(input("\nGuess a number between 1-100: "))

        if User_guess > comp_numb:
            print("\nYour guess is high ⬆")
        elif User_guess < comp_numb:
            print("\nYour guess is low ⬇")
        elif User_guess == comp_numb:
            print(f"\nCongrats your guess is right the number is {comp_numb} 🏆")  
            break
        else:
            print("\nplease write a valid number.")

        #Lives remaining
        Numb_of_tries -= 1 
        print(f"\nLives remaining: {Numb_of_tries}")

        if Numb_of_tries == 0:
            ask = input("\nWant to play again? (Y/N): ").lower() 
            if ask != "y":
                print(f"\nOut of tries! The correct number was {comp_numb}. Better luck next time!")
            else:
                Numb_guessing_game()
             

Numb_guessing_game()