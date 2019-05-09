"""
@author: jocelin - RYJ
"""
import math

def bezout_coefs(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u, v = bezout_coefs(b, a % b)
        return gcd, v, u - (a // b) * v


def find(rx, ry, x, y):
    pg, x00, y00 = bezout_coefs(ry, rx)
    x0 = x00 * (rx * y - ry * x)
    y0 = - y00 * (rx * y - ry * x)
    x1 = - y00 * (x * rx - y * ry)
    y1 = x00 * (x * rx - y * ry)
    k = max(math.ceil(-x0 / rx), math.ceil(-y0 / ry))
    k2 = max(math.ceil(-y1 / rx), math.ceil(-x1 / ry))
    xp0 = rx * k + x0
    xp1 = ry * k2 + x1
    pgcd = (x + xp0) // rx
    pgcd2 = (x + xp1) // ry
    yp0 = ry * pgcd - y
    yp1 = rx * pgcd2 - y
    xp, yp, K = 0, 0, 1
    if (x + xp0) * (y + yp0) < (x + xp1) * (y + yp1):
        xp, yp = xp0, yp0
    elif (x + xp0) * (y + yp0) > (x + xp1) * (y + yp1):
        xp, yp, K = xp1, yp1, 2
    else:
        if xp0 < xp1:
            xp, yp = xp0, yp0
        elif xp0 > xp1:
            xp, yp, K = xp1, yp1, 2
        else:
            xp, yp = xp0, yp0
    X, Y = (x + xp, y + yp)
    return ((X, Y), K) if K == 1 else ((Y, X), K)


def comp(a, b):
    (w1, h1), k1 = a
    (w2, h2), k2 = b
    if (w1 * h1) > (w2 * h2):
        return b
    elif (w1 * h1) < (w2 * h2):
        return a
    else:
        if w1 > w2:
            return b
        elif w1 < w2:
            return a
        else:
            if k1 > k2:
                return b
            else:
                return a


with open('picture.in') as f:
    pgcd = lambda a, b: a if b == 0 else pgcd(b, a % b)
    for _ in range(int(f.readline())):
        print('Case %d:' % (_ + 1))
        ratios = []
        for i in range(int(f.readline())):
            ratios.append(tuple(map(int, f.readline().split())))
        keep = 0
        for i in range(int(f.readline())):
            best = None
            ln = f.readline().rstrip()
            x, y = map(int, ln.split())
            for ratio in ratios:
                rx, ry = ratio
                pg = pgcd(x, y)
                xp, yp = x // pg, y // pg
                r = 0
                if (xp, yp) == (rx, ry):
                    r = (x, y), 0
                elif (yp, xp) == (rx, ry):
                    r = (y, x), 1
                else:
                    (w, h), k = best if best is not None else ((1, 1), None)
                    if k == None or (w * h) > (rx * ry):
                        r = find(rx, ry, x, y)
                    else:
                        keep += 1
                if r != 0:
                    best = r if best is None else comp(best, r)
            (w, h), k = best
            print(w, h, k)