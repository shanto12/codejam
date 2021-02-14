for t in range(1, int(input())+1):
    N=int(input())
    SE_dict = dict()
    # k, r, c = 0, 0, 0
    for row in range(N):
        S, E = map(int, input().split())
        SE_dict.setdefault(S, dict())
        SE_dict[S][row] = E


    # SE_dict_new=dict()
    # for S, E_list in sorted(SE_dict.items()):
    #     SE_dict_new[S] = sorted(E_list, reverse=True)


    # SE_list.sort(key=lambda tup: tup[0])

    C, J = 0, 0
    solution_list=[""]*N
    solution=None
    for S, E_dict in sorted(SE_dict.items()):
        for index, E in sorted(E_dict.items(), key=lambda item: item[1], reverse=True):
            # for E in E_list:
            if C<=S:
                solution_list[index]="C"
                C=E
            elif J<=S:
                solution_list[index]="J"
                J = E
            else:
                solution="IMPOSSIBLE"
                break

    if not solution:
        solution = "".join(solution_list)


    print(f"Case #{t}: {solution}")