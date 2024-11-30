'''
AUTHOR: ELLEN JOY
DATE:30/11/2024
PROGRAM TO CHECK WHETHER THE GIVEN NUMBER IS A MOBILE NUMBER OR NOT
'''

def mobile_number(num):
    if len(num)==10 and num[0] in "789":
        print("This is a mobile number")
    else:
        print("This is not a mobile number")
num=input("Enter your mobile number:")
mobile_number(num)


