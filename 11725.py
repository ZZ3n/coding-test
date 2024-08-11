# 루트 없는 트리
# 트리 루트를 1이라고 정했을 때,
# 각 노드의 부모를 구하는 프로그램 작성

# 노드 개수 2 <= N <- 100_000
from collections import deque


def find_parent(graph):
    parent = [-1] * len(graph)
    Q = deque()
    Q.append(1)

    visited = [False] * len(graph)
    while Q:
        now = Q.pop()
        visited[now] = True
        for vert in graph[now]:
            if not visited[vert]:
                parent[vert] = now
                Q.append(vert)
    return parent


N = int(input())
edges = [[] for i in range(N + 1)]

for i in range(N - 1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

result = find_parent(edges)
for i in range(2, N + 1):
    print(result[i])
