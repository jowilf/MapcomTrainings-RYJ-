from math import log

filename = 'tree.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        h, l = map(int, f.readline().strip().split(" "))
        grow_end_height = 1 + int(log(l, 2))
        result = 1
        for level in range(1, grow_end_height):
            result += 2 ** level
        result += l * (h + 1 - grow_end_height)
        print(f"Case {i+1}: {result}")
