import os
from time import sleep

def UP():
    height = 5

    for i in range(1, height+1):

        for j in range(0,3,1):
            print("\t\t\t", end="")
        for j in range(height-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()
    for i in range(1, height+1):
        for j in range(0,3,1):
            print("\t\t\t", end="")
        for j in range(height-1):
            print(" ", end="")

        print("*", )







def Down():
    height = 5

    for i in range(1, 5+1):
        for j in range(0,3,1):
            print("\t\t\t", end="")
        for j in range(5-1):
            print(" ", end="")
            
        print("*", )
    


    for i in range(4, 0, -1):
        for j in range(0,3,1):
                print("\t\t\t", end="")
        for j in range(5-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()




def Left():
    height = 4

    for i in range(1, height+1):
        for j in range(0,3,1):
                print("\t\t\t", end="")
        for j in range(height-i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()

    print("\t\t\t\t\t\t\t\t\t************")
    for i in range(height-1, 0, -1):
        for j in range(0,3,1):
                print("\t\t\t", end="")
        for j in range(height-i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()




def Right():
    height = 4



    for i in range(height):
        for j in range(0,3,1):
                print("\t\t\t", end="")
        for j in range(i+1):
            print("* ", end="")
        print()
    print("\t\t\t\t\t\t\t* * * * * * * * * * * * *")
    for i in range(height, 0, -1):
        for j in range(0,3,1):
                print("\t\t\t", end="")
        for j in range(0, i):
            print("* ", end=" ")

        print()






while True:  
    UP()
    sleep(0.3)
    os.system('cls')
    Right()
    sleep(0.3)
    os.system('cls')
    Down()    
    sleep(0.3)
    os.system('cls')
    Left()
    sleep(0.3)
    os.system('cls')