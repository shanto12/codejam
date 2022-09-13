for t in range(1, int(input()) + 1):
    N = int(input())
    S_list = [int(x) for x in input().split()]

    #
    # for i in range(N):
    #     j = L[i:j + 1].index(min(L[i:j + 1]))
    #     j = j + i
    #     L = L[:i] + L[i:j + 1][::-1] + L[j + 1:]
    #     cost += j - i + 1
    #
    # print(f"Case #{t}: {cost}")
