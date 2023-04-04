import copy

# block world bfs implemenetation

visited = []
reached = []


def enqueue(s):
    reached.append(s)


def dequeue():
    state = reached[0]
    del reached[0]
    return state


def compare(s, goal):
    for i in range(len(s)):
        if s[i] not in goal:
            return False
    return True


def genChild(s, goal):
    for i in range(len(s)):
        parent = copy.deepcopy(s)
        if parent[i]:
            block = parent[i][-1]
            del parent[i][-1]
            for j in range(len(parent)):
                if j != i:
                    state = copy.deepcopy(parent)
                    state[j].append(block)
                    if compare(state, goal):
                        print("Goal reached!")
                        print(len(visited))
                        exit(0)
                    flag = 1
                    for elem in visited:
                        if compare(elem, state):
                            flag = 0
                    for elem in reached:
                        if compare(elem, state):
                            flag = 0
                    if flag:
                        enqueue(state)
    visited.append(s)


def dfs(start, goal):
    state = copy.deepcopy(start)
    while 1:
        genChild(state, goal)
        if len(reached) == 0:
            return print("Goal not found!")
        state = dequeue()


def main():
    start = [['A'], ['B', 'C'], []]
    goal = [['A', 'B', 'C'], [], []]
    dfs(start, goal)


main()
