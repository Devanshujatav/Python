numbers=[1,2,3,4,5]

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

# print(list[:3])

# list.append(7)
# list.insert(6,6)

# print(list)


numbers.extend([9,8,7,6])
# print("List before removing element : ")
# print(list)

# list.remove(9)
# print("list after removing element : ")
# print(list)

# lastElement = list.pop()
# print(lastElement)
#
# print(list)

# list.clear()

print("List :",numbers)
print("Length of the List :",len(numbers))
numbers.sort()
print("List after sorting :",numbers)
numbers.reverse()
print("List after get reverse :",numbers)

print(numbers.index(5))

print("count of 5 in the list :",numbers.count(5))

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(matrix[2][2])

cubes = [x**3 for x in range(1,6)]
print(cubes)