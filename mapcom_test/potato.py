"""
@author: jocelin - RYJ
"""
def is_possible(c, i, arr):
    if c == 0:
        return True
    if c < 0 or i >= len(arr):
        return False
    else:
        return is_possible(c - arr[i], i + 1, arr) or is_possible(c, i + 1, arr)


with open('potato.in') as f:
    for _ in range(int(f.readline())):
        line = list(map(int, f.readline().split()))
        K, n, arr = line[0], line[1], line[2:]
        print(f'{K} {"YES" if is_possible(n,0,arr) else "NO"}')
    f.close()
