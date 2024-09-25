# 인접 배추도 보호 가능, 상하좌우

# 인접 배추가 몇 군데 있는지
# 필요한 지렁이 개수는?

from collections import deque


def get_worm_cnt(mat, arr):
    not_visited = deque(arr)
    visited = set()
    worn_cnt = 0
    while not_visited:
        starting = not_visited.pop()
        if starting in visited:
            continue
        Q = deque()
        Q.append(starting)
        while Q:
            pos = Q.popleft()
            visited.add(pos)
            y, x = pos
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < len(mat) and 0 <= nx < len(mat[0]):
                    if mat[ny][nx] == 1 and (ny, nx) not in visited:
                        Q.append((ny, nx))
            # 주변에 배추가 없는 경우
            # print(f"pos = {pos}, Q = {Q}")
        worn_cnt += 1
    return worn_cnt

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for j in range(N)]
    arr = []
    for i in range(K):
        pos_x, pos_y = map(int, input().split())
        arr.append((pos_y, pos_x))
        matrix[pos_y][pos_x] = 1
    print(get_worm_cnt(matrix, arr))
