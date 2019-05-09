"""
@author: jocelin - RYJ
"""
class Problem:
    def __init__(self, _id):
        self.id = id
        self.teams = set()


class Team:
    def __init__(self, _id):
        self.id = id
        self.problems = set()


class Time:
    def __init__(self, t):
        self.h, self.m, self.s = map(int, t.split(':'))
        self.str = t

    def __repr__(self):
        return self.str

    def __lt__(self, other):
        if self.h == other.h:
            if self.m == other.m:
                return self.s < other.s
            else:
                return self.m < other.m
        else:
            return self.h < other.h

    def __eq__(self, other):
        if type(other) == Time:
            return self.str == other.str
        return False


def idc(c):
    return ord(c) - ord("A")


with open('marathon.in') as f:
    T, P, S = map(int, f.readline().split())
    while (T, P, S) != (0, 0, 0):
        teams = [Team(i) for i in range(T)]
        problems = [Problem(i) for i in range(P)]
        submissions = []
        start_time, end_time, last_end = None, None, 0
        last_decision = False
        for i in range(S):
            line = f.readline().split()
            tId, pId, time, result = int(line[0]) - 1, idc(line[1]), Time(line[2]), line[3]
            submissions.append((tId, pId, time, result))
        submissions.sort(key=lambda k: k[2])
        i = 0
        for tId, pId, time, result in submissions:
            if result == "Yes":
                problems[pId].teams.add(tId)
                teams[tId].problems.add(pId)
            # check cond3-4
            cond3, cond4 = True, True
            for problem in problems:
                cond3 = cond3 and len(problem.teams) > 0
                cond4 = cond4 and len(problem.teams) < T
                if not cond3 or not cond4:
                    break
            # check  cond1-2
            cond1, cond2 = True, True
            if cond3 and cond4:
                for team in teams:
                    cond1 = cond1 and len(team.problems) > 0
                    cond2 = cond2 and len(team.problems) < P
                    if not cond1 or not cond2:
                        break
            if cond1 and cond2 and cond3 and cond4:
                if start_time == None:
                    start_time = time
                end_time = submissions[i + 1][2] if (i + 1) < S else '--:--:--'
                last_end = i
            i += 1
        if start_time == None:
            print('--:--:-- --:--:--')
        else:
            print(start_time, end_time)
        T, P, S = map(int, f.readline().split())
