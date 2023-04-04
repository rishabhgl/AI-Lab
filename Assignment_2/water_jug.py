import copy

capacity = [4, 3]
reached = []
visited = []


def enqueue(s):
    global reached
    reached += [s]


def dequeue():
    global reached
    state = reached[0]
    del reached[0]
    return state


def pop():
    global reached
    state = reached[-1]
    del reached[-1]
    return state


def compare(s, goal):
    if s in goal:
        return True
    else:
        return False


def fillx(parent):
    s = copy.deepcopy(parent)
    if s[0] < 4:
        s[0] = 4
    return s


def filly(parent):
    s = copy.deepcopy(parent)
    if s[1] < 3:
        s[1] = 3
    return s


def throwx(parent):
    s = copy.deepcopy(parent)
    if s[0] > 0:
        s[0] = 0
    return s


def throwy(parent):
    s = copy.deepcopy(parent)
    if s[1] > 0:
        s[1] = 0
    return s


def transferxtoy(parent):
    s = copy.deepcopy(parent)
    if s[0] > 0:
        if s[0] + s[1] <= 3:
            s[1] += s[0]
            s[0] = 0
        else:
            s[0] = s[0] - (3 - s[1])
            s[1] = 3
    return s


def transferytox(parent):
    s = copy.deepcopy(parent)
    if s[1] > 0:
        if s[0] + s[1] <= 4:
            s[0] += s[1]
            s[1] = 0
        else:
            s[1] = s[1] - (4 - s[0])
            s[0] = 4
    return s


def traversebfs(start, goal):
    global visited, reached
    s = copy.deepcopy(start)
    while 1:
        new = filly(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(visited)
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = fillx(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = transferytox(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = transferxtoy(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = throwx(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = throwy(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        visited += [s]
        if len(reached) != 0:
            s = dequeue()
        else:
            print("Goal state could not be reached")
            return False


def traversedfs(start, goal):
    global visited, reached
    s = copy.deepcopy(start)
    while 1:
        new = filly(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(visited)
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = fillx(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = transferytox(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = transferxtoy(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = throwx(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        new = throwy(s)
        if new != s:
            if compare(new, goal):
                print("Found the goal state!")
                print(len(visited))
                return True
            if new not in visited and new not in reached:
                enqueue(new)
        visited += [s]
        if len(reached) != 0:
            s = pop()
        else:
            print("Goal state could not be reached")
            return False


def main():
    global visited
    start = [0, 0]
    goal = []
    for i in range(capacity[1] + 1):
        goal += [[2, i]]
    traversebfs(start, goal)
    visited = []
    traversedfs(start, goal)


main()
