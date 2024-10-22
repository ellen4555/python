'''
Author : Ellen joy
date : 22/10/2024
Program is to convert celsius to fahrenheit and fahrenheit to celsius temperature
'''
temperature=int(input("Enter the temperature:"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
if(unit=="C"):
    f=(9/5)*(temperature+32)
    print(temperature,"Celsius is",f,"Fahrenheit")
else:
    c=(5/9) *(temperature-32)
    print(temperature,"fahrenheit is",c,"celsius")


