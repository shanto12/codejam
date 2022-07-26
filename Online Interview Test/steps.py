N = int(input(f"enter the number of steps: "))
step_length_list = [int(x.strip()) for x in (input(f"enter the length of steps: ").split(","))]

print(f"{N}, {step_length_list}")

def find_no_of_ways(steps, step_length_list):
    length=0
    for ste_length in step_length_list:
        if steps>=ste_length:
            length+=1+find_no_of_ways(steps-ste_length, step_length_list)

    return length

print(find_no_of_ways(N, step_length_list))