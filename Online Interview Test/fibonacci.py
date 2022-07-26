def fibonacci(n):
    print(f"Here with n: {n}")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(int(input(f"Enter value for N: "))))
