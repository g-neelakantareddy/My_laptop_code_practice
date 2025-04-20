import os


def print_directories(startpath, indent=""):
    for item in os.listdir(startpath):
        item_path = os.path.join(startpath, item)
        print(indent+"|--"+item)

        if os.path.isdir(item_path):
            print_directories(item_path, indent="|  ")


directory_path = 'C:\\Karthik'
print_directories(directory_path)
