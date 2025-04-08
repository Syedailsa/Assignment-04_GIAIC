import random

#random numbers from 1 to 100
numbers = [random.randint(1,100) for _ in range(10)]

#storing all 10 numb in list
random_numbers = list(numbers)

for i in random_numbers:
    print(i)