points = {1: {1: "T", 2: "M", 3: "F"},
          2: {1: "U", 2: "N", 3: "G", 4: "A"},
          3: {1: "V", 2: "O", 3: "H", 4: "B"},
          4: {1: "W", 2: "P", 3: "I", 4: "C"},
          5: {1: "X", 2: "Q", 3: "J", 4: "D"},
          6: {1: "Y", 2: "R", 3: "K", 4: "E"},
          7: {1: "Z", 2: "S", 3: "L"}}

letters = {'T': {'x': 1, 'y': 1}, 'M': {'x': 1, 'y': 2}, 'F': {'x': 1, 'y': 3},
           'U': {'x': 2, 'y': 1}, 'N': {'x': 2, 'y': 2}, 'G': {'x': 2, 'y': 3},
           'A': {'x': 2, 'y': 4}, 'V': {'x': 3, 'y': 1}, 'O': {'x': 3, 'y': 2},
           'H': {'x': 3, 'y': 3}, 'B': {'x': 3, 'y': 4}, 'W': {'x': 4, 'y': 1},
           'P': {'x': 4, 'y': 2}, 'I': {'x': 4, 'y': 3}, 'C': {'x': 4, 'y': 4},
           'X': {'x': 5, 'y': 1}, 'Q': {'x': 5, 'y': 2}, 'J': {'x': 5, 'y': 3},
           'D': {'x': 5, 'y': 4}, 'Y': {'x': 6, 'y': 1}, 'R': {'x': 6, 'y': 2},
           'K': {'x': 6, 'y': 3}, 'E': {'x': 6, 'y': 4}, 'Z': {'x': 7, 'y': 1},
           'S': {'x': 7, 'y': 2}, 'L': {'x': 7, 'y': 3}}

def get_intersection_points_between(sl,el):
    sp, ep= letters[sl], letters[el]
    i_points = list()
    #y=ax+b
    a = 0
    diff_x = ep["x"]-sp["x"]
    if (diff_x != 0):
        a = (ep["y"]-sp["y"])/(diff_x)
        b = ep["y"]-a*ep["x"]
        #intersections with vertical axes
        min_x, max_x = min(sp["x"],ep["x"]), max(sp["x"],ep["x"])
        x = min_x+0.5
        while(x<max_x):
            y = round(a*x+b,10)
            if x%1==y%1==0.5:
                i_points.append({"x": x, "y": y, "axe": "both"})
            else:
                i_points.append({"x": x, "y": y, "axe": "vertical"})
            x+=1
        #intersections with horizontal axes
        min_y, max_y = min(sp["y"],ep["y"]), max(sp["y"],ep["y"])
        y = min_y+0.5
        while(y<max_y):
            x = round((y-b)/a,10)
            if not x%1==y%1==0.5:
                i_points.append({"x": x, "y": y, "axe": "horizontal"})
            y+=1
    else:
        #intersections with horizontal axes
        min_y, max_y = min(sp["y"],ep["y"]), max(sp["y"],ep["y"])
        y = min_y+0.5
        while(y<max_y):
            i_points.append({"x": sp["x"], "y": y, "axe": "horizontal"})
            y+=1
    #align points
    i_points.sort(key = lambda p: (p["x"]-sp["x"])**2+(p["y"]-sp["y"])**2)
    return i_points

def get_potential_letters(p):
    l = set()
    if p["axe"]=="vertical":
        x1, x2, y = int(p["x"]-0.5), int(p["x"]+0.5), int(p["y"]+0.5) 
        l = set()
        if x1 in points.keys() and y in points[x1].keys(): l.add(points[x1][y])
        if x2 in points.keys() and y in points[x2].keys(): l.add(points[x2][y])
    elif p["axe"]=="horizontal":
        x, y1, y2 = int(p["x"]+0.5), int(p["y"]-0.5), int(p["y"]+0.5)
        l = set()
        if x in points.keys():
            if y1 in points[x].keys(): l.add(points[x][y1])
            if y2 in points[x].keys(): l.add(points[x][y2])
    else:
        x1, x2, y1, y2 = int(p["x"]-0.5), int(p["x"]+0.5), int(p["y"]-0.5), int(p["y"]+0.5)
        l = set()
        if x1 in points.keys():
            if y1 in points[x1].keys(): l.add(points[x1][y1])
            if y2 in points[x1].keys(): l.add(points[x1][y2])
        if x2 in points.keys():
            if y1 in points[x2].keys(): l.add(points[x2][y1])
            if y2 in points[x2].keys(): l.add(points[x2][y2])
    return l

def get_path(possible_letters_sets):
    p = ""
    for i in range(-1+len(possible_letters_sets)):
        intersect = list(possible_letters_sets[i].intersection(possible_letters_sets[1+i]))
        p+=intersect[0]
    return p

def expanse_seg(poly_segment):
    start_letter, end_letter = poly_segment
    pts = get_intersection_points_between(start_letter, end_letter)
    lts = list(map(get_potential_letters,pts))
    path = get_path(lts)
    if len(path)>=1:
        if path[0]==start_letter: path = path[1:]
        if path[-1]==end_letter: path = path[:-1]
    return start_letter+path+end_letter

def expanse(poly_line):
    expansion = poly_line[0]
    for letter_idx in range(-1+len(poly_line)):
        poly_segment_expanded = expanse_seg(poly_line[letter_idx:letter_idx+2])
        expansion += poly_segment_expanded[1:]
    return expansion

def is_subseq(seq,sub):
    start = 0
    for letter in sub:
        found = False
        for idx, l in enumerate(seq[start:]):
            if l==letter:
                start += 1+idx
                found = True
                break
        if not found:
            return False
    return True

filename = 'keyboard.in'
with open(filename, 'r') as f:
    number_of_test_cases = int(f.readline())
    for i in range(number_of_test_cases):
        n, poly_line = f.readline().strip().split(" ")
        n = int(n)
        expansion = expanse(poly_line)
        found = False
        for word_idx in range(n):
            word = f.readline().strip()
            if not found and is_subseq(expansion,word):
                print(word)
                found = True
        if not found:
            print("NO SOLUTION")