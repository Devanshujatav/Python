def printList(list1 , idx=0):
    if(idx == len(list1)):
        return
    print(list1[idx] , end=" ")
    printList(list1 , idx+1)


list2= [1,2,3,4,5]

printList(list2)