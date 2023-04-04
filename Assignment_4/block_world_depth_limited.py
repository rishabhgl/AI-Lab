import copy

# block world depth limited search implementation

visited = []
reached = []
depthTree = 1


def enqueue(s):
    reached.append(s)


def dequeue():
    state = reached[-1]
    del reached[-1]
    return state


def compare(s, goal):
    for i in range(len(s)):
        if s[i] not in goal:
            return False
    return True


def genChild(s, goal, depth):
    visited.append(s)
    level = s[0]
    element = s[1]
    if level == depth:
        return
    for i in range(len(element)):
        parent = copy.deepcopy(element)
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
                        enqueue([level + 1, state])


def dfs(start, goal, depth):
    state = copy.deepcopy(start)
    state = [0, state]
    while 1:
        genChild(state, goal, depth)
        if len(reached) == 0:
            return print("Goal not found!")
        state = dequeue()


def main():
    global visited
    start = [['A'], ['B', 'C'], []]
    goal = [['A', 'B', 'C'], [], []]
    dfs(start, goal, depthTree)
    len_before = len(visited)
    visited = []
    dfs(start, goal, depthTree + 1)
    len_after = len(visited)
    if len_after > len_before:
        print('Depth limited search with depth', depthTree, 'is not complete')


main()
