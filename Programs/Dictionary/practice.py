student={
    "name":"alice",
    "age":"23",
    "grade":"A"
}

# print(student["name"])

# print(student.get("name"))
# print(student.get("age"))
# print(student.get("grade"))

student["major"]="computer science"
student["grade"]="A+"
# print(student)

del student["age"]

dict2={
    "age":"23",
    "gender":"female"
}

grade=student.pop("grade")
# print(student)
# print(grade)

# print(student.get("name"))
# print(student.keys())
# print(student.values())
# print(student.items())
student.update(dict2)
# print(student)

age = student.pop("age")
c=student.popitem()
# print(c)
# print(student)
# print(age)

# student.clear()
# print(student)

# for key in student:
#     print(key)

# for value in student.values():
#     print(value)

# for key , value in student.items():
#     print({key} , {value})
#
# for key , value in student.items():
#     print(f"{key} : {value}")

# students = {
#     "student1" : {"name": "alice" , "age":23},
#     "student2" : {"name": "Bob" , "age" : 24}
# }
#
# print(students["student1"]["name"])

# text = "hello world"
# charCount = {}
# for char in text:
#     charCount[char]=charCount.get(char,0)+1
#
# print(charCount)

dict={
    "Table" : "A piece of furniture list of facts and figures" ,
    "Cat" : "A small animal"
}

print(dict.items())