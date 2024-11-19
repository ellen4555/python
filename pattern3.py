'''
Author: Ellen joy
increasing triangle
'''
limit=int(input("Enter a limit:"))
for  number in range(1,limit):
    for number2 in range(limit-number):
        print(" ",end=" ")
    for number3 in range(1,2*number):
        print("*",end=" ")
    print()

