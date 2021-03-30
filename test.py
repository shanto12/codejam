mylist = [6, 4, 2, 8, 1]

i, j = 2, 4
mylist = mylist[:i] + mylist[i:j+1][::-1] + mylist[j+1:]


print(mylist)