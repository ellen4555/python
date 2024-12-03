#multiplying two numbers using recursion
def product(n1,n2):
    if n2 == 1:
        return n1
    else:
        return n1+product(n1,n2-1)
n1=int(input("Enter num1: "))
n2=int(input("Enter num2: "))
print(product(n1,n2))