from collections import deque

# 토마토
# M * N
# 익은 토마토 인접(4) 토마토는 익는다.
# 며칠이 지나야 다 익는지? (최소 일수)
# 상자 크기, 익은 토마토, 안익은 토마토

M, N = map(int, input().split())
MAP = []
RIPEN = 1
FRESH = 0

Q = deque()
for n in range(N):
    lane = list(map(int, input().split()))
    for m in range(M):
        if lane[m] == RIPEN:
            Q.append((n, m, 0))
    MAP.append(lane)


result = 0
while Q:
    n, m, t = Q.popleft()
    for dn, dm in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nn = n + dn
        nm = m + dm
        nt = t + 1
        if nn < 0 or nn >= N or nm < 0 or nm >= M:
            continue
        if MAP[nn][nm] == FRESH:
            MAP[nn][nm] = RIPEN
            Q.append((nn, nm, nt))
            if nt > result:
                result = nt


for n in range(N):
    for m in range(M):
        if MAP[n][m] == FRESH:
            result = -1
            break
    if result == -1:
        break
    
print(result)