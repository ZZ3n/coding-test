# 연결된 정점을 쭉 따라갔을 때, 1이 있으면 부모, 아니면 자식이다.
from collections import deque

N = int(input())
MAP = []
for i in range(N - 1):
    a, b = map(int, input().split())
    MAP.append((a, b))

parents = [0 for i in range(N + 1)]


def find_parent(graph):
    global parents
    queue = deque()
    visited = set()
    queue.append(1)
    while queue:
        now = queue.pop()
        visited.add(now)
        for edge in graph:
            if edge[0] == now and edge[1] not in visited:
                parents[edge[1]] = now
                queue.append(edge[1])
            if edge[1] == now and edge[0] not in visited:
                parents[edge[0]] = now
                queue.append(edge[0])

find_parent(MAP)
for i in range(2, N + 1):
    print(parents[i])
