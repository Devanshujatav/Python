# from dataclasses import replace
# from operator import truediv
# from tkinter.scrolledtext import example
# from traceback import print_tb
#
# from flask.json.tag import JSONTag
#
# file = open("example.txt" , "r")
# # data = file.readlines()
# # print(data)
#
#
# # Read Operation on File
# with open("example.txt" , "r") as file:
#     content = file.readlines()
#     # print(content)
#
# # Write Operation on File
#
# # Write Operation on a single line
# with open("example.txt" , "w") as file:
#     file.write("hello developer")
#
# # Write Operation on Multiple Lines
# with open("example.txt" , "w") as file:
#     file.writelines(["Hello World \n " , "I am a Developer \n"])
#
# with open("example.txt" , "a") as file:
#     file.write("Appended Text \n.")
#
# file = open("example.txt" , "r")
# content = file.read()
# # print(content)
#
# with open("example.txt" , "a+") as file:
#     file.seek(23)
#     position = file.tell()
#     # print(file.read())
#     # print(position)
#
# with open("840934.jpg" , "rb") as img:
#     img.read()
#     # print(img)
#
#
#
# with open("practice.txt" , "w") as f:
#     f.writelines(["Hii Everyone \n" , "We are learning File I/O \n" , "using Java. \n" , "I like programming in Java \n"])
#
# with open("practice.txt" , "r") as f:
#     data = f.read()
#
# newData = data.replace("Java" , "Python")
# # print(newData)
#
# with open("practice.txt" , "w") as f:
#     f.write(newData)
#
#
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if (data.find(word) != -1):
#             print("found")
#         else:
#             print("Not Found")

# def check_for_line():
#     data = True
#     line = 1
#     word = "learning"
#     with open("practice.txt" , "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line+=1
#
#     return -1
#
# check_for_line()



# def count_even():
#     count=0
#     with open("practice.txt" , "r") as f:
#         data = f.read()
#         nums = data.split(",")
#         for val in nums:
#             if(int(val)%2==0):
#                 count+=1
#     print(count)
#
#
# count_even()


# with open("example.txt" , "w") as file:
#     file.write("now its get edited\n")
#     file.writelines(["Hii , I am Devanshu Jatav\n" , "I am an Innovator\n"])
#
# with open("example.txt" , "r") as file:
#     file.seek(10)
#     print(file.tell())
#     print(file.read())


# with open("840934.jpg" , "rb") as file:
#     data = file.read()
#     print(data)
#

# try:
#     with open("non_existence.txt" , "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")


with open("practice.txt" , "w") as file:
    value = file.writelines(["Hii Everyone \n" , "we are learning FileI/O \n" , "using Java\n" , "I like programming in Java."])

# with open("practice.txt" , "r") as file:
#     data = file.read()
#
# # new_data = data.replace("Java" , "Python")
#
# with open("destination.txt" , "w") as file:
#     data2 = file.write(data)
#     # print(data2)

# def countWords():
#     count = 0;
#     with open("practice.txt" , "r") as file:
#         data = file.read()
#         for i in range(len(data)):
#             count+=1
#
#         print(count)
#
#
# countWords()

def wordExists():
    word = "programming"
    with open("practice.txt" , "r") as file:
        data = file.read()

        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

wordExists()