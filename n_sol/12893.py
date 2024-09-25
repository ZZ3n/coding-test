# a - b b - c
# a + c

# a - b, b - c => a + c
# c - d => a - d
# d - e => a + e

# a - b + c

# 1 2
# 2 3
# 3 4
# 4 5

from collections import deque

N, M = map(int, input().split())
edges = {i: [] for i in range(1, N + 1)}

for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def find(target):
    global edges
    Q = deque()
    Q.append((target, 0))
    enemy = []
    friend = []
    visited = set()
    while Q:
        current, depth = Q.pop()
        visited.add(current)
        for v in edges[current]:
            if v in visited:
                Q.append((v, depth + 1))
                if depth % 2 == 0:
                    enemy.append(v)
                else:
                    friend.append(v)

    print(f"target {target} | enemy {enemy} | friend {friend}")
    return enemy, friend

#1 2 3
# 1 2
# 2 3

for i in range(1, N + 1):
    print(find(i))
