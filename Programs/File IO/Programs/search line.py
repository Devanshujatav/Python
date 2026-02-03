def searchLine():
    lineNo = 1
    data = True
    word = "programming"
    with open("practice.txt", "r") as file:
        while (data):
            data = file.readline()
            if (word in data):
                print(lineNo)
                return
            lineNo += 1
    return -1


searchLine()