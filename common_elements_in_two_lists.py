list_1 = [1, 2, 4, 5, 6, 7]
list_2 = [3, 6, 7, 8, 2, 1]
list_3 = [2, 8, 6]
list_4 = [2, 6, 8]
common_elements_list = []
for i in list_1:
    if i in list_2 and i in list_3 and i in list_4:
        common_elements_list.append(i)
print(common_elements_list)
