'''
author : Ellen Joy
Program to remove duplicates from a list
date : 19/11/2024
'''


my_list=[1,2,3,4,5,6,3,2,1]
unique_list=[]
for number in my_list:
    if number not in unique_list:
        unique_list.append(number)
print("The orginal list is",my_list)
print(unique_list)