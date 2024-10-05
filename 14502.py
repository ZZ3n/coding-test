# 0 중 3개를 골라 벽을 세움
# 각 2에서 BFS 진행.
# 0 세기
from collections import deque
from pprint import pprint
from itertools import combinations

N, M = map(int, input().split())
MAP = []
for i in range(N):
    MAP.append(list(map(int, input().split())))

viruses = []
walls = []
rooms = []
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            rooms.append((i, j))
        if MAP[i][j] == 1:
            walls.append((i, j))
        if MAP[i][j] == 2:
            viruses.append((i, j))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(fac):
    global viruses, walls
    Q = deque(viruses)
    while Q:
        y, x = Q.pop()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and fac[ny][nx] == 0:
                fac[ny][nx] = 2
                Q.append((ny, nx))
    return fac


def empty_count(fac):
    empty_cnt = 0
    for i in range(N):
        for j in range(M):
            if fac[i][j] == 0:
                empty_cnt += 1
    return empty_cnt


def make_new_map(returnable_map, new_walls):
    global rooms, MAP

    for y in range(N):
        for x in range(M):
            returnable_map[y][x] = MAP[y][x]
    for wy, wx in new_walls:
        returnable_map[wy][wx] = 1
    return returnable_map

new_map = [[0] * M for _ in range(N)]

result = 0
for combo in combinations(rooms, 3):
    make_new_map(new_map, combo)
    bfs(new_map)
    cnt = empty_count(new_map)
    if cnt > result:
        result = cnt
print(result)


"""
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 1 0 0 2
"""
