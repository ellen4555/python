'''
AUTHOR: ELLEN JOY
DATE:30/11/2024
counting the uppercase and lower case charachters in a string
'''

def count_upper_lower_case_characters(input_string):
    upper_characters=0
    lower_characters=0
    for i in input_string:
        if i.isupper():
            upper_characters += 1
        if i.islower():
            lower_characters += 1
    return upper_characters,lower_characters
input_string=input("Enter a string:")
upper_characters,lower_characters=count_upper_lower_case_characters(input_string)
print(upper_characters)
print(lower_characters)



