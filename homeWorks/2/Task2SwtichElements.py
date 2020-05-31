my_list = list(input("Fill the list: "))
buffer_list = []
switched_copy_of_my_list = []
for ind, el in enumerate(my_list):
    if (ind % 2 == 0) and (ind != 0):
        buffer_list.reverse()
        switched_copy_of_my_list.extend(buffer_list)
        buffer_list.clear()
    buffer_list.append(el)
    if ind == (len(my_list) - 1):
        buffer_list.reverse()
        switched_copy_of_my_list.extend(buffer_list)
        my_list.clear()
        my_list = switched_copy_of_my_list
print(my_list)
