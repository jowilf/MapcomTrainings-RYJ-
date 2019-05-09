import math


def solve(a, b, c, d, e, f):
    if (a * e - b * d) != 0:
        x = (c * e - b * f) / (a * e - b * d)
        y = ((c - a * x) / b) if b != 0 else ((f - d * x) / e)
        return x, y
    return None, None


class Point:
    def __init__(self, x, y):
        self.x, self.y = round(x, 10), round(y, 10)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def tuple(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def vector(a, b):
    return Point(b.x - a.x, b.y - a.y)


class Hexagon:
    def __init__(self, center: Point, length):
        self.center = center
        self.length = length
        self.a = length
        self.h = math.sqrt(3) * (self.a / 2)
        a, x, y = length, center.x, center.y
        h = self.h
        self.p1, self.p2, self.p3, self.p4, self.p5, self.p6 = Point(x - a / 2, y + h), Point(x + a / 2, y + h), Point(
            x + a, y), Point(x + a / 2, y - h), Point(x - a / 2, y - h), Point(x - a, y)
        self.points = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]
        self.points.reverse()
    def tuple(self):
        return self.center.tuple()

    def childs(self):
        a, h, x, y = self.a, self.h, self.center.x, self.center.y
        return Point(x, y + 2 * h), Point(x, y - 2 * h), Point(x - 3 * a / 2, y + h), Point(
            x + 3 * a / 2, y + h), Point(x - 3 * a / 2, y - h), Point(x + 3 * a / 2, y - h)

    # This algo check if points is inside any of 6 equilateral triangles of hexagons
    def is_inside(self, m: Point):
        for i in range(len(self.points)):
            a, b, c = self.points[i], self.points[(i + 1) if i < len(self.points) - 1 else 0], self.center
            t, tp = solve(b.x - a.x, c.x - a.x, m.x - a.x, b.y - a.y, c.y - a.y, m.y - a.y)
            if 0 <= t <= 1 and 0 <= tp <= 1 and (t + tp) <= 1:
                return True
        return False

    def __eq__(self, other):
        return self.center == other.center

    def __repr__(self):
        return f'Hex({self.center})'


def bfs(node, p):
    fringe = [node]
    close = {}
    aNode = None
    dist = {}
    dist[node.tuple()] = 0
    while len(fringe) > 0:
        node = fringe.pop(0)
        if not close.get(node.tuple(), False):
            if node.is_inside(p):
                aNode = node
                break
            else:
                for ci in node.childs():
                    child = Hexagon(ci, node.length)
                    if dist.get(node.tuple(), float('inf')) + vector(child.center, node.center).norm() < dist.get(
                            child.tuple(), float('inf')):
                        dist[child.tuple()] = dist[node.tuple()] + vector(child.center, node.center).norm()
                        fringe.append(child)
            close[node.tuple()] = True
            fringe.sort(key=lambda h: dist.get(h.tuple(), float('inf')))
    return aNode, dist.get(aNode.tuple())


with open('hexagon.in') as f:
    l, xA, yA, xB, yB = map(float, f.readline().split())
    while (l, xA, yA, xB, yB) != (0, 0, 0, 0, 0):
        A, B = Point(xA, yA), Point(xB, yB)
        # find hexagon who contains A
        aNode, _ = bfs(Hexagon(Point(0, 0), l), A)
        # find hexagon who contains B
        bNode, d = bfs(aNode, B)
        if aNode == bNode:
            print('%.3f' % vector(A, B).norm())
        else:
            print('%.3f' % (d + vector(A, aNode.center).norm() + vector(B, bNode.center).norm()))
        l, xA, yA, xB, yB = map(float, f.readline().split())
