my_list = [7, 5, 3, 3, 2]
num = int(input("Enter the N: "))
if num in my_list:
    position_to_insert = my_list.index(num) + my_list.count(num)
    my_list.insert(position_to_insert, num)
else:
    for ind, el in enumerate(my_list):
        if num > el:
            my_list.insert(ind, num)
            break
        elif num < my_list[-1]:
            my_list.insert(len(my_list), num)
print(my_list)
