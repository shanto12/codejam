for t in range(1, int(input())+1):
    N=int(input())
    matrix = []
    k, r, c = 0, 0, 0
    for row in range(N):
        row_list = list(map(int, input().split()))
        if len(set(row_list)) != N:
            r += 1
        matrix.append(row_list)
    for i in range(N):
        k += matrix[i][i]
        c_list = []
        for j in range(N):
            c_list.append(matrix[j][i])

        if len(set(c_list)) != N:
            c += 1

    print(f"Case #{t}: {k} {r} {c}")