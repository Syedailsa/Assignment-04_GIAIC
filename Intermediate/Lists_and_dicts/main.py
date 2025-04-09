print("Problem #1: List Practice")
#Now practice writing code with lists! Implement the functionality described in the comments below.

#def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 


# Print the updated list.

print("###########################################################################")

#ANSWER

fruit_list: str = ["apple", "banana", "orange", "grape", "pineapple"]
print(f"\nOriginal Fruit List: {fruit_list}")

#length if list
print(f"\nLength of Original fruit list: {len(fruit_list)}")

#adding mango at the end
fruit_list.append("mango")

#updated list
print(f"\nUpdated Friut List: {fruit_list}")
print(" ")


print("Problem #2: Index Game")

print("###########################################################################")

#ANSWER

#initializing a list

car_list = ["honda brv", "prado", "honda city", "kia", "honda civic", "toyota corolla", "suzuki alto"]


def List_game():

    play = True
    while play:

        ask = input("What do you want to do with the list of cars: \n1.Find the car with index no? \n2.Modify existing car with another car? \n3.Slice the list?\nEnter your choice: ")

        if ask == "1":
            #input for index in list
            index = int(input("\nwrite an index no you want to know the car for: "))

            if 0 <= index < len(car_list):
                print(f"\nCar at index {index} is: {car_list[index].capitalize()}")
            else: 
                print("\nindex out of range")

        elif ask == "2":
            #input for index in list
            index = int(input("\nwrite an index no you want to know the car for: "))   

            #new value for the index
            new_val = input(f"Write the name of car you want to replace {car_list[index]} with: ")
            
            if 0 <= index < len(car_list):
                print(f"\nCar at index {index} was: {car_list[index].capitalize()}")
                car_list[index] = new_val
                print(f"\nCar at index {index} is now: {car_list[index].capitalize()}")

            else: 
                print("\nindex out of range")

        elif ask == "3":

            #input for start slicing in list
            start_index = int(input("\nwrite an index you want to start slicing for:  "))

            #input for end slicing in list
            end_index = int(input("\nwrite an index you want to end slicing for:  ")) 
            
            if 0 <= start_index < len(car_list) and 0<= end_index <= len(car_list):

                print(f"\nCar list before: {car_list}")

                #slicing
                sliced_list = car_list[start_index:end_index]
                print(f"\nCar list now: {sliced_list}")

            else: 
                print("\nindex out of range")

        else:
            print("Not valid choice")
        
        continue_play = input("\nDo you want to do something else? (Y/N): ").lower()

        if continue_play != "y":
            play = False



List_game()