# 뱀과 사다리 게임

# 1 ~ 6
# 10 x 10
# 1 ~ 100까지 적혀있음
# i, 4 => i+4

# 칸 넘어가면 못 감
# 사다리면 타고 위로 올라감 (번호가 커짐 > GOOD)
# 뱀 있으면 뱀 타고 내려감 (번호가 작아짐 > BAD)
from collections import deque


def foo(ladders, snakes):
    Q = deque()
    Q.append((0, 1))
    visited = set()
    while Q:
        dice, pos = Q.popleft()
        visited.add(pos)
        if pos == 100:
            return dice

        for i in range(1, 7):
            if (pos + i) == 100:
                Q.append((dice + 1, pos + i))
            if pos + i in visited:
                continue
            if pos + i in ladders.keys():
                Q.append((dice + 1, ladders[pos + i]))
                continue
            if pos + i in snakes.keys():
                Q.append((dice + 1, snakes[pos + i]))
                continue
            Q.append((dice + 1, pos + i))


N, M = map(int, input().split())
ladders = {}
snakes = {}
for i in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

for i in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

print(foo(ladders, snakes))
