# Ao-star algorithm

edge = 1


def node_cost(heuristic, children):
    cost = {}
    if 'OR' in children:
        or_children = children['OR']
        for child in or_children:
            cost[child] = heuristic[child] + edge
    if 'AND' in children:
        and_children = children['AND']
        cost['AND'] = 0
        for child in and_children:
            cost['AND'] += heuristic[child] + edge
    return cost


def cost(heuristic, tree):
    nodes = list(tree.keys())
    nodes.reverse()
    for node in nodes:
        parent_cost = node_cost(heuristic, tree[node])
        heuristic[node] = min(list(parent_cost.values()))


def main():
    start = 'a'

    heuristic = {
        'a': 50,
        'b': 6,
        'c': 12,
        'd': 10,
        'e': 4,
        'f': 4,
        'g': 5,
        'h': 7
    }

    tree = {
        'a': {'OR': ['d'], 'AND': ['b', 'c']},
        'b': {'OR': ['g', 'h']},
        'd': {'AND': ['e', 'f']}
    }
    cost(heuristic, tree)
    print('The cost of traversal of tree using AO* algorithm:', heuristic['a'])


main()
