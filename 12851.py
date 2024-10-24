from collections import deque

N, K = map(int, input().split())

result = (0, 0)
path = [0] * 100_001
cnt = 0

Q = deque()
Q.append(N)

while Q:
    pos = Q.popleft()

    if pos == K:
        result = path[pos]
        cnt += 1
        continue

    for new_pos in [pos - 1, pos + 1, pos * 2]:
        if new_pos > 100_000 or new_pos < 0:
            continue
        if path[pos] + 1 == path[new_pos] or path[new_pos] == 0:
            path[new_pos] = path[pos] + 1
            Q.append(new_pos)

print(result)
print(cnt)
