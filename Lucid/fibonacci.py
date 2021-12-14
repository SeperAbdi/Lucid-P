
# I am using recursive method to calculate the number
def fib_to(n):
    if n < 0:
        print("Incorrect Input!")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_to(n-1) + fib_to(n-2)

print(fib_to(10))