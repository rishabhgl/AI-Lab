import copy

q = []
visited = []


def enqueue(s):
    global q
    q += [s]


def dequeue():
    state = q[0]
    del q[0]
    return state


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


def traversebfs(start, goal):
    global visited, q
    s = copy.deepcopy(start)
    while 1:
        new = up(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in q:
                enqueue(new)
        new = down(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in q:
                enqueue(new)
        new = right(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in q:
                enqueue( new)
        new = left(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in q:
                enqueue( new)
        visited.append(s)
        if len(q) != 0:
            s = dequeue()
        else:
            print("Goal state could not be reached")
            return False


def traversedfs(start, goal):
    global visited, q
    s = copy.deepcopy(start)
    while 1:
        new = up(s)
        if compare(new, goal):
            print("Found the goal state!")
            print(len(visited))
            return True
        if new not in visited:
            enqueue(new)
        new = down(s)
        if compare(new, goal):
            print("Found the goal state!")
            print(len(visited))
            return True
        if new not in visited:
            enqueue(new)
        new = right(s)
        if compare(new, goal):
            print("Found the goal state!")
            print(len(visited))
            return True
        if new not in visited:
            enqueue(new)
        new = left(s)
        if compare(new, goal):
            print("Found the goal state!")
            print(len(visited))
            return True
        if new not in visited:
            enqueue(new)
        visited.append(s)
        if len(q) != 0:
            s = pop()
        else:
            print("Goal state could not be reached")
            return False


def main():
    start = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]
    goal = [[0, 8, 1],
             [4, 2, 3],
             [7, 6, 5]]
    traversebfs(start, goal)


main()
