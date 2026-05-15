while True:
    s = input("Enter a Strings : ")
    if s == s[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")