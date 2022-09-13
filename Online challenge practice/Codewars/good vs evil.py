text = """"
Hobbits: 1
Men: 2
Elves: 3
Dwarves: 3
Eagles: 4
Wizards: 10
On the side of evil we have:

Orcs: 1
Men: 2
Wargs: 2
Goblins: 2
Uruk Hai: 3
Trolls: 5
Wizards: 10
"""

good_text, evil_text = text.split("On the side of evil we have:")

good_dict = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in good_text.split("\n") if
             line and ":" in line}

evil_dict = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in evil_text.split("\n") if
             line and ":" in line}

print(good_dict)
print(good_dict.values())
print(evil_dict.values())


def good_vs_evil(good, evil):
    good_value_list = [1, 2, 3, 3, 4, 10]

    good_total = 0
    for count, v in zip(good.split(), good_value_list):
        good_total += v * int(count)

    evil_value_list = [1, 2, 2, 2, 3, 5, 10]
    evil_total = 0
    for count, v in zip(evil.split(), evil_value_list):
        evil_total += v * int(count)

    if good_total > evil_total:
        return f"Battle Result: Good triumphs over Evil"
    elif good_total == evil_total:
        return f"Battle Result: No victor on this battle field"
    else:
        return f"Battle Result: Evil eradicates all trace of Good"



print(good_vs_evil('1 1 1 1 1 2', '1 1 1 1 1 1 2'))
