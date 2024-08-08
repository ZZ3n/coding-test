# 정사각형
# TL에서 시작
# 오른쪽 or 아래
# BR에 도달하면 승리
# 밟고 있는 칸 수 만큼 이동 가능

from collections import deque


def dfs(graph):
    stack = deque()
    stack.append((0, 0))
    visited = set()
    while stack:
        y, x = stack.pop()
        visited.add((y, x))
        value = graph[y][x]
        if (value == -1):
            return "HaruHaru"
        if (y + value) < N and not (y + value, x) in visited:
            stack.append((y + value, x))
        if (x + value) < N and not (y, x + value) in visited:
            stack.append((y, x + value))
    return "Hing"


N = int(input())
MAP = [list(map(int, input().split())) for i in range(N)]

print(dfs(MAP))
