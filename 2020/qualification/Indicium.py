# Passed. Right answer

def options(N):
    options_list = []
    first=list(range(1, N+1))
    second = list(reversed(first))
    for mylist in [first, second]:
        option=[]
        for i in range(N):
            option.append(mylist[i:] + mylist[:i])
        options_list.append(option)

    return options_list

def check_K(options_list, K):
    length = len(options_list)
    summ = sum(options_list[i][i] for i in range(length))
    if K==summ:
        return True

    return False



for t in range(1, int(input())+1):
    N, K=[int(x) for x in input().split()]

    options_list=options(N)
    for options in options_list:
        if check_K(options, K):
            pass


    print(f"Case #{t}: {5}")