from collections import deque

N, M = map(int, input().split())

visited = [False for _ in range(N + 1)]
visited[0] = True
result = 0

MAP = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    MAP[u].append(v)
    MAP[v].append(u)

Q = deque()
for i in range(N + 1):
    if visited[i] == True:
        continue
    Q.append(i)
    visited[i] = True
    while Q:
        node = Q.popleft()
        for adj in MAP[node]:
            if visited[adj]:
                continue
            Q.append(adj)
            visited[adj] = True
    result += 1
print(result)
