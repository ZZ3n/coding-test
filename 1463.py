from collections import deque

N = int(input())


def bfs(n):
    Q = deque()
    Q.append((n, 0))
    while Q:
        x, d = Q.popleft()
        if x == 1:
            return d

        if x % 3 == 0:
            Q.append((x // 3, d + 1))
        if x % 2 == 0:
            Q.append((x // 2, d + 1))
        Q.append((x - 1, d + 1))


print(bfs(N))
