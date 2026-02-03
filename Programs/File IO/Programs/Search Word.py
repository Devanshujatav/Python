def check_for_word():
    word = "programming"
    with open("practice.txt", "r") as file:
        data = file.read()
        # print(data)
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")

check_for_word()