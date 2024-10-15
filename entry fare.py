'''
author : Ellen joy
date : 15-10-2024
program to determine the entr fare based on age
'''
age=int(input("Enter your age:"))
if(age<10):
    print("Fair is 7")
elif(age>=10 and age<=60):
    print("Fare is 10")
else:
    print("Fare is 5")
