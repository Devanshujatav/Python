with open("practice.txt" , "r") as source:
    data = source.read()

with open("destination.txt" , "w") as destination:
    destination.write(data)
    print(destination)
