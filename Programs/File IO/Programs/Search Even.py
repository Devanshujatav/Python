def countEven():
    count = 0
    with open("practice.txt" , "r") as file:
        data = file.read()
        list1 = data.split(",")
        for val in list1:
           if (int(val)%2==0):
               count+=1

        print(count)
    return

countEven()