a=int(input("Enter the First Number : "))
b=int(input("Enter the Second Number : "))
c=int(input("Enter the Third Number : "))

if((a>b) and (a>c)):
    print(a , " is greater than", b , " and ", c)
elif((b>a) and (b>c)):
    print(b , " is greater than ", a ,  " and ", c)
else:
    print(c , "is greater than ", a , " and ", b)
