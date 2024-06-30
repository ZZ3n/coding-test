from collections import deque

N, M, V = map(int, input().split())


def DFS(edges, start):
    visited = [False] * (N + 1)
    visited[0] = True
    Q = deque()
    Q.append(start)
    while Q:
        now = Q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        print(now, end=" ")
        canGo = []
        for edge in edges:
            if edge[0] == now:
                canGo.append(edge[1])
            if edge[1] == now:
                canGo.append(edge[0])
        canGo.sort(reverse=True)
        Q.extendleft(canGo)
    print()

def BFS(edges, start):
    visited = [False] * (N + 1)
    visited[0] = True
    Q = deque()
    Q.append(start)
    while Q:
        now = Q.popleft()
        if visited[now]:
            continue
        visited[now] = True
        print(now, end=" ")
        canGo = []
        for edge in edges:
            if edge[0] == now:
                canGo.append(edge[1])
            if edge[1] == now:
                canGo.append(edge[0])
        canGo.sort()
        for dest in canGo:
            Q.append(dest)


edges = []
for i in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

DFS(edges, V)
BFS(edges, V)
