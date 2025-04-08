import time

#Count down
Count_down: int = [5, 4, 3, 2, 1]

print("\nSpaceship is going to take off in..")

for i in Count_down:
    print(i)
    time.sleep(1) #it will pause for 1 sec before executing the other

print("Lift Off..🚀")  