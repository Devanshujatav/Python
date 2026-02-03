def countWords():
    count = 0
    with open("practice.txt", "r") as file:
        data = file.read()
        # print(data)
        for i in range(len(data)):
            count+=1
        print(count)
    return


countWords()