numbers = (1,4,9,16,25,36,49,64,81,100)
value=int(input("Enter the Target Value : "))

i=0

while(i<len(numbers)):
    if(value in numbers):
        print("Element Found")
        break
    else:
        print("Element Not Found")
        break
    i+=1