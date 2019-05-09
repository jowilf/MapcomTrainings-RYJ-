from collections import Counter

filename = 'robot.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        occurences = dict(Counter(f.readline().strip()))
        motions = {"R": 0, "U": 0, "?": 0}
        for key, value in occurences.items():
            if key == "R":
                motions["R"]+=value
            elif key == "L":
                motions["R"]-=value
            elif key == "U":
                motions["U"]+=value
            elif key == "D":
                motions["U"]-=value
            elif key == "?":
                motions["?"] = value
        x_min = motions["R"] - motions["?"]
        y_min = motions["U"] - motions["?"]
        x_max = motions["R"] + motions["?"]
        y_max = motions["U"] + motions["?"]
        print(f"{x_min} {y_min} {x_max} {y_max}")