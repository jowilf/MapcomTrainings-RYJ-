"""
@author: jocelin - RYJ
"""
import bisect

with open('ordering.in') as f:
    for _ in range(int(f.readline())):
        line = list(map(int, f.readline().split()))
        K, arr = line[0], line[1:]
        order = []
        step_back = 0
        while len(arr) > 0:
            student = arr.pop(0)
            idx = bisect.bisect(order, student)
            step_back += len(order) - idx
            order.insert(idx, student)
        print(f'{K} {step_back}')
    f.close()
