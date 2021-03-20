# Passed but wrong answer

for t in range(1, int(input())+1):
    S=[int(x) for x in input()]
    S_ = ""
    counter = S[0]
    previous = S[0]
    S_ += "(" * counter
    S_ += str(S[0])
    for number in S[1:]:
        diff=number-previous
        if diff==0:
            S_ += str(number)
            # counter = 0
            previous = number
        elif diff <0:
            S_ += ")" * abs(diff)
            S_ += str(number)
            counter = counter-abs(diff)
            previous = number
        else:
            S_ += ")" * counter
            counter = number
            S_ += "(" * counter
            S_ += str(number)
            previous = number

    S_ += ")" * counter

    print(f"Case #{t}: {S_}")