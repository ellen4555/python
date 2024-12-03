#adding two numbers using recursion
def add_numbers(n1,n2):
    if n2 == 0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
n1=2
n2=3
print(add_numbers(n1,n2))
