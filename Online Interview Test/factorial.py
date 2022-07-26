def factorial(n):
    print(f"Here with n: {n}")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(int(input(f"Enter value for N: "))))
