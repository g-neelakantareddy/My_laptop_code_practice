with open('details.txt','w') as file:
    file.write("9866242188\n")
    file.write("@neela143")
with open('details.txt', 'r') as file:
    read = file.readlines()
    print(type(read[0]))
