import copy

q = []
visited = []


def enqueue(s):
    global q
    q += [s]


def dequeue():
    global q
    state = False
    for i in range(len(q)):
        if q[i][0] < visited[-1][0]:
            state = q[i]
    q.clear()
    if state:
        return state[1]
    return 0



def pop():
    state = q[-1]
    del q[-1]
    return state


def compare(s, g):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]: # S,G are 3X3 matrices
                return False
    return True


def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]
    return 0


def up(start):
    s = copy.deepcopy(start)
    pos = find_pos(s)
    if pos[0] > 0:
        s[pos[0]][pos[1]] = s[pos[0] - 1][pos[1]]
        s[pos[0] - 1][pos[1]] = 0
        return s
    return s


def down(start):
    s = copy.deepcopy(start)
    pos = find_pos(s)
    if pos[0] < 2:
        s[pos[0]][pos[1]] = s[pos[0] + 1][pos[1]]
        s[pos[0] + 1][pos[1]] = 0
        return s
    return s


def left(start):
    s = copy.deepcopy(start)
    pos = find_pos(s)
    if pos[1] > 0:
        s[pos[0]][pos[1]] = s[pos[0]][pos[1] - 1]
        s[pos[0]][pos[1] - 1] = 0
        return s
    return s


def right(start):
    s = copy.deepcopy(start)
    pos = find_pos(s)
    if pos[1] < 2:
        s[pos[0]][pos[1]] = s[pos[0]][pos[1] + 1]
        s[pos[0]][pos[1] + 1] = 0
        return s
    return s


def heuristic(state, goal):
    counter = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                counter += 1
    return counter


def traverseHillClimb(start, goal):
    global visited, q
    s = copy.deepcopy(start)
    while 1:
        new = up(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            enqueue([heuristic(new,goal),new])
        new = down(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            enqueue([heuristic(new,goal),new])
        new = right(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            enqueue([heuristic(new,goal),new])
        new = left(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited:
                enqueue([heuristic(new,goal),new])
        visited.append([heuristic(s,goal),s])
        s = dequeue()
        if s == 0:
            print("Goal state could not be reached")
            print(len(visited))
            return False


def main():
    goal = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]
    start = [[2, 8, 3],
             [1, 5, 4],
             [7, 6, 0]]
    traverseHillClimb(start, goal)


main()
