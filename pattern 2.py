limit=int(input("Enter a limit:"))
for  number in range(limit):
    for number2 in range(limit-number):
        print("*",end=" ")
    print()