def fibonacci(n, memo=[0, 1, 1]):
    print(f"Here with n: {n}")
    if n > len(memo)-1:
        memo.append(fibonacci(n - 1, memo) + fibonacci(n - 2, memo))

    print(f"Returning: {memo[n]}")
    return memo[n]


print(fibonacci(int(input(f"Enter value for N: "))))
