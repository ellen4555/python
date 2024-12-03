#program to find greatest common divisor(gcd) of two numbers
def gcd(n1,n2):
    if n1%n2 == 0:
        return n2
    else:
        return gcd(n2,n1%n2)
n1=int(input("Enter num1: "))
n2=int(input("Enter num2: "))
print(gcd(n1,n2))