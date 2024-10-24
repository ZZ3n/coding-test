from collections import deque

N, K = map(int, input().split())


maxi = abs(K - N)
result = (0, 0)
visited = set()

Q = deque()
Q.append((N, 0))

while Q:
    pos, sec = Q.popleft()
    if sec > maxi:
        continue

    if pos == K:
        maxi = sec
        result = (sec, result[1] + 1)
        continue

    for new_pos in [pos - 1, pos + 1, pos * 2]:
        if 0 < pos and pos > 100_001:
            continue
        if sec + 1 > maxi:
            continue
        Q.append((new_pos, sec + 1))

print(result[0])
print(result[1])
