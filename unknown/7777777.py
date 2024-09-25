# 수빈 N
# 동생 K
# 걷는다면 X+1, X-1
# 순간이동 X*2로 이동

# 수빈, 동생 위치 => 가장 빠른 시간
from collections import deque


def find(N, K):
    Q = deque()
    Q.append((0, N))
    visited = set()
    while Q:
        now, pos = Q.popleft()
        visited.add(pos)
        if pos == K:
            return now

        if pos - 1 >= 0 and pos - 1 not in visited:
            Q.append((now + 1, pos - 1))
        if pos + 1 <= 100_000 and pos + 1 not in visited:
            Q.append((now + 1, pos + 1))
        if pos * 2 <= 100_000 and 2 * pos not in visited:
            Q.append((now + 1, 2 * pos))


N, K = map(int, input().split())

sec = find(N, K)
print(sec)