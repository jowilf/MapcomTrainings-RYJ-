def remind(a, b, e=0):
    sum, rem_ = a + b + e, 0
    if sum >= 10:
        sum -= 10
        rem_ = 1
    return sum, rem_


with open('sum.in') as f:
    n = int(f.readline())
    while n > 0:
        a, b, c = f.readline().rstrip(), f.readline().rstrip(), f.readline().rstrip()
        a, b, c = list(map(int, list(a))), list(map(int, list(b))), list(map(int, list(c)))
        n = len(a)
        connects = [0] * n
        end = n - 1
        reminder = [None] * n
        for i in range(n):
            sum, rem = remind(a[i], b[i])
            if sum == c[i]:
                reminder[i] = rem
                connects[i] += 1
                end = i
        for i in range(end - 1, -1, -1):
            for j in range(end, i, -1):
                if reminder[j] != None:
                    isum, irem = remind(a[i], b[i], reminder[j])
                    if isum == c[i] and connects[i] < connects[j] + 1:
                        connects[i] = connects[j] + 1
                        reminder[i] = irem
        connect_max = 0
        for i in range(n):
            if reminder[i] == 0:
                connect_max = max(connect_max, connects[i])
        print(n - connect_max)
        n = int(f.readline())