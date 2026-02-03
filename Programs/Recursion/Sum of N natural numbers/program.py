def Nsum(n):
    if (n==0):
        return 0
    return Nsum(n-1)+n

sum=Nsum(3)
print(sum)