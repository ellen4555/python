'''
author: Ellen joy
date: 15/10/2024
program to determine the sum of three digits
'''
number=int(input("Enter the number:"))
sum=0
while(number>0):
    r=number%10
    number=number//10
    sum=sum+r
print("sum of digits:",sum)
