from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(ox, oy, M, N, sym, MAP):
    Q = deque()
    Q.append((ox, oy))
    while Q:
        x, y = Q.pop()
        if MAP[x][y] == -1:
            MAP[x][y] = sym
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or nx >= M:
                continue
            if ny < 0 or ny >= N:
                continue
            if MAP[nx][ny] != -1:
                continue
            Q.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    baechu_pos_list = list()
    MAP = [[0 for j in range(N)] for i in range(M)]

    for k in range(K):
        # 0 <= x < M, 0 <= y < N
        x, y = map(int, input().split())
        MAP[x][y] = -1
        baechu_pos_list.append((x, y))

    result = 0
    for k in range(K):
        x, y = baechu_pos_list[k]
        if MAP[x][y] != -1:
            continue
        result += 1 
        bfs(x, y, M, N, result, MAP)
        

    # print(MAP)
    print(result)
