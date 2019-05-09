with open('base.in') as f:
    for _ in range(int(f.readline())):
        k, n = f.readline().split()
        oct_ = 0
        try:
            oct_ = int(n, 8)
        except:
            pass
        print(f'{k} {oct_} {int(n,10)} {int(n,16)}')
    f.close()
