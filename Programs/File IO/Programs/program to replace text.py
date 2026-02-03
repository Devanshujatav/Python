with open("practice.txt" , "r") as file:
    data = file.read()
    # print(data)
new_data = data.replace("Java","Python")
# print(new_data)

with open("practice.txt" , "w") as file:
    data = file.write(new_data)
    print(data)