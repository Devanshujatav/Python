with open("practice.txt" , "a") as file:
    data = file.write(" \nFile handling is easy!")
    print(data)

with open("practice.txt" , "r") as file:
    data = file.read()
    print(data)