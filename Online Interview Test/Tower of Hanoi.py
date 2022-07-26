def toh(n, start, end, aux):
    if (n == 1):
        print("Move disk 1 from", start, "to", end)
        return
    toh(n - 1, start, aux, end)
    print("Move disk", n, "from", start, "to", end)
    toh(n - 1, aux, end, start)


n = int(input("Enter the number of disks: "))
toh(n, 'A', 'B', 'C')
