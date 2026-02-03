from math import factorial


def fact_rec(num):
    if num ==1:
        return 1
    else:
        factorial = num * fact_rec(num-1)
        return factorial
num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {fact_rec(num)}")