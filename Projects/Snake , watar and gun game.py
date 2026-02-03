import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1 , 0 , 1])

# USER CHOICE INPUT
youStr = input("Enter your choice : ")

# DICTIONARY FOR GAME PROTOCOLS
youDict = {
    "S" : 1,
    "W" : -1 ,
    "G" : 0
}

# REVERSE DICTIONARY IS USED TO GIVE USER CHOSEN OUTPUT
reverseDict = {
    1 : "Snake",
    -1 : "Water" ,
    0 : "Gun"
}

# Variable for give reference to dictionary and produce an output
you = youDict[youStr]

if(computer == you):
    print("Its a Draw")

else:
    if(computer == -1 and you == 1):
        print("You WIN")
    elif(computer == -1 and you==0):
        print("You Lose")
    elif(computer==1 and you == -1 ):
        print("You Lose")
    elif(computer==1 and you == -1):
        

