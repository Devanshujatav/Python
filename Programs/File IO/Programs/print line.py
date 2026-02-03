with open("practice.txt" , "r") as file:
    data = file.readlines()
    # print(data)
    # print(len(data))\
    #
    # for i in range(len(data)):
    #     print(i , data[i])
    i=1
    print("Line No.         Line Data")
    for val in data:
        print("  ", i ,"        ", val)
        i+=1