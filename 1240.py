from collections import deque

N, M = map(int, input().split())
edges = {i: [] for i in range(1, N + 1)}


def find_value(a, b):
    global edges
    Q = deque()
    Q.append((a, 0))
    visited = set()
    while Q:
        vert, dist = Q.popleft()
        visited.add(vert)
        if vert == b:
            return dist
        for v, d in edges[vert]:
            if v not in visited:
                Q.append((v, dist + d))


for i in range(N - 1):
    a, b, v = map(int, input().split())
    edges[a].append((b, v))
    edges[b].append((a, v))

result = []
for i in range(M):
    a, b = map(int, input().split())
    result.append(find_value(a, b))

for r in result:
    print(r)