import itertools

N = 10000
sum = list(itertools.accumulate(range(1, N + 1)))
even = list(itertools.accumulate(range(1, 2 * N + 1, 2)))
odd = list(itertools.accumulate(range(2, 2 * N + 1, 2)))
# print(sum, even, odd, sep='\n')
with open('sum.in') as f:
    for _ in range(int(f.readline())):
        k, n = map(int, f.readline().split())
        print(f'{k} {sum[n-1]} {even[n-1]} {odd[n-1]}')
    f.close()
