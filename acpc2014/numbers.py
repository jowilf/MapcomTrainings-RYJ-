"""
@author: jocelin - RYJ
"""
f = open('numbers.in', 'r')
t = int(f.readline())
for _ in range(t):
    x, n, y, m = map(int, f.readline().split())
    A, B = 0, x
    for i in range(n):
        tmp = A
        A = B
        B += tmp
        if A > B:
            A, B = B, A
    B += y
    pgcd = lambda a, b: a if b == 0 else pgcd(b, a % b)
    print('Case %d: %d' % (_ + 1, pgcd(A, B)))
f.close()
