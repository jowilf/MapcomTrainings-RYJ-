"""
@author: yannick - RYJ
"""


def stones(n, m, x):
    if (n > m):
        if (n % m == 0 and m == x) or n % m == x:
            print("YES")
        else:
            print("NO")
    elif (n <= m):
        if (n == x):
            print("YES")
        else:
            print("NO")


filename = 'stone.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        a, b, c = map(int, f.readline().strip().split())
        stones(int(a), int(b), int(c))
