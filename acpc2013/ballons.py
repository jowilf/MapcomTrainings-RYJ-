with open('balloons.in', 'r') as f:
    for _ in range(int(f.readline())):
        n, x, y = f.readline().split()  # map(int, input())
        a = f.readline().split()
        n = len(a)
        if (a[0] == x and a[n - 1] == y):
            print("BOTH")
        if (a[0] == x and a[n - 1] != y):
            print('EASY')
        if (a[0] != x and a[n - 1] == y):
            print("HARD")
        if (a[0] != x and a[n - 1] != y):
            print("OKAY")
