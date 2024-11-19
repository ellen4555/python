'''
Author: Ellen joy
decreasing triangle
'''

limit=int(input("Enter a limit:"))
for  number in range(limit):
    for number2 in range(limit+number):
        print(" ",end=" ")
    for number3 in range((2*limit)-(2*number)-1):
        print("*",end=" ")
    print()