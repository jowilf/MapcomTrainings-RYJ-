"""
@author: romaric - RYJ
"""
with open('tawla.in') as f:
    T = int(f.readline())
    Ts = []
    for i in range(T):
        Ts.append(list(f.readline().split()))


    def tala(a, b):
        tmp = min(a, b)
        a = max(a, b)
        b = tmp
        c = 0
        if a == b:
            c = a
        di = {1: "Yakk", 2: "Doh", 3: "Seh", 4: "Ghar", 5: "Bang", 6: "Sheesh"}
        if (a == 6 and b == 5):
            name = "Sheesh Beesh"
        elif a == b:
            if c == 1:
                name = "Habb Yakk"
            elif c == 2:
                name = "Dobara"
            elif c == 3:
                name = "Dousa"
            elif c == 4:
                name = "Dorgy"
            elif c == 5:
                name = "Dabash"
            elif c == 6:
                name = "Dosh"
        else:
            name = di[a] + " " + di[b]
        return name


    for i in range(T):
        a = "Case %d: %s" % (i + 1, tala(int(Ts[i][0]), int(Ts[i][1])))
        print(a)
