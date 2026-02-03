numbers = (1,4,9,16,25,36,49,64,81,100)
tar=int(input("Enter the Target Value : "))
idx =0
for val in numbers:
    if(val == tar):
        print("Element Found at index ",idx)
        break
    idx+=1


