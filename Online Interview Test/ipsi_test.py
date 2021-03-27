N, K = map(int, input().split())

A = sorted(list(map(int, input().split())), reverse=True)

path = [N]
for factor in A:
    if N % factor == 0:
        N = N//factor
        path.append(N)
    if N == 1:
        break
else:
    path = [-1]

print(" ".join(map(str, sorted(path))))

