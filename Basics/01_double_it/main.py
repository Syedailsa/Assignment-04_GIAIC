#double the numb

curr_value = int(input("Write a number: "))
new_val = []

while curr_value <= 100:

    double_it = curr_value * 2
    new_val.append(double_it)
    curr_value = double_it

for i in new_val:
    print(i)
    

