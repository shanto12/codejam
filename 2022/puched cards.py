for t in range(1, int(input()) + 1):
    next_lines = input().split(" ")
    R, C = next_lines[0], next_lines[1]
    L = [int(x) for x in input().split()]
    cost = 0
    j = N - 1
    for i in range(N):
        j = L[i:j + 1].index(min(L[i:j + 1]))
        j = j + i
        L = L[:i] + L[i:j + 1][::-1] + L[j + 1:]
        cost += j - i + 1

    print(f"Case #{t}: {cost}")
