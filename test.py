def solution(S):
    # write your code in Python 3.6
    a=S[0]
    result = True
    for s in S[1:]:
        if a>s:
            result = False
            break
        else:
            a=s
    return result

print(solution("ba"))