"""
@author: yannick - RYJ
"""
from itertools import accumulate

filename = 'sum.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        n, m = map(int, f.readline().strip().split(" "))
        grid = list()
        for _ in range(n):
            values = map(int, f.readline().strip().split(" "))
            grid.append(list(accumulate(values)))
        score = -2001
        for col_idx in range(m-2,-1,-1):
            #m-2 to 0
            s = 0
            for row_idx in range(n-1,-1,-1):
                #n-1 to 0
                s += grid[row_idx][m-1] - grid[row_idx][col_idx]
                score = max(score,s)
        s = 0
        for row_idx in range(n-1,-1,-1):
            #n-1 to 0
            s += grid[row_idx][m-1]
            score = max(score,s)
        print(score)
            
            