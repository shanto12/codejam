for t in range(1, int(input())+1):
    N=int(input())
    L = [int(x) for x in input().split()]
    cost=0
    for i in range(N):
        j = L.index(min(L))
        L[i:j+1].reverse()
        cost += j-i + 1

    print(f"Case #{t}: {cost}")