def bezout_coefs(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u, v = bezout_coefs(b, a % b)
        return gcd, v, u - (a // b) * v


def swap(a, b):
    return b, a


def ilen(a, b):
    import math
    return int(b) - math.ceil(a) + 1


def interval_len(a=0, b=0, ferm1=True):
    if ferm1:
        return int(b) - int(a) + (1 if int(b) != b else 0)
    else:
        return int(b) - int(a) + (1 if int(a) != a else 0)


# pref = 'acpc2013-IO-J/'
# out = open(pref + 'sequence.out', 'r').readlines()
with open('sequence.in', 'r') as f:
    for _ in range(int(f.readline())):
        n1, f1, d1, n2, f2, d2 = map(int, f.readline().split())
        if f2 == f1:
            print(min(interval_len(b=n1 * d1 / d2), interval_len(b=n2 * d2 / d1)))
            # print('->', ans, out[_].replace('\n', ''))
        else:
            pgcd, x1, x2 = bezout_coefs(d1, d2)
            x = f1 + x1 * d1 * (f2 - f1) // pgcd
            ppcm = (d2 * d1) // pgcd
            l1 = (f1 - x) / ppcm
            r1 = (f1 + d1 * (n1 - 1) - x) / ppcm
            l2 = (f2 - x) / ppcm
            r2 = (f2 + d2 * (n2 - 1) - x) / ppcm
            # print(min(interval_len(l1, r1), interval_len(l2, r2))
            # print(l1, r1, l2, r2)
            r = min(ilen(l1, r1), ilen(l2, r2))
            print(r)
