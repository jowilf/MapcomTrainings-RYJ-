"""
@author: jocelin - RYJ
"""
import itertools

N = 10000
acc = list(itertools.accumulate(range(2, N + 2)))
# print(acc)
with open('challenge.in') as f:
    for _ in range(int(f.readline())):
        k, n = map(int, f.readline().split())
        print(f'{k} {acc[n-1]}')
    f.close()
