def solution(s):
    import textwrap

    mylist = textwrap.wrap(s, 2)

    if mylist and len(mylist[-1]) == 1:
        mylist[-1] = mylist[-1] + "_"

    return mylist


print(solution("shantos"))
