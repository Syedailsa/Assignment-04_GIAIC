import random

print("\nWelcome to the High-Low Game!")
print("-"*50)

def High_Low():

    rounds = 1
    points = 0

    game = True

    while game:

        print(" ")
        print("="*50)
        print(" ")
        print(f"Round No {rounds}:")
        
        
        #random nim for computer
        Comp_num = random.randint(1,100)

        #random nim for user
        User_num = random.randint(1,100)

        #user input
        Guess = input("\nGuess if your number is HIGHER or LOWER than opponents number: ").lower()
        
        if User_num > Comp_num and Guess == "higher":
            print(f"\nCongrats you`re right your number is higher then opponents number {Comp_num} 💚")
            points += 1
            print(f"\nYour points: {points}")  
        elif User_num < Comp_num and Guess == "lower":
            print(f"\nCongrats you`re right your number is lower then opponents number {Comp_num} 💚")
            points += 1
            print(f"\nYour points: {points}")  
        else: 
            print(f"\nYou`re wrong the opponents numbers is {Comp_num}")
            print(f"\nYour points: {points}")  

        rounds += 1

        if rounds == 4:
            if points == 3:
                print("Wow! You played perfectly!")
            elif points == 2 or 1:
                print("Good job, you played really well!")
            else:
                print("Better Luck Next Time! 😊")  
                
            ask = input("\nWant to play again? (Y/N): ").lower() 
            if ask != "y":
                print(" ")
                print(f"Total Points: {points}\nGood plying 💟")
                game = False
            else:
                High_Low()

High_Low() 