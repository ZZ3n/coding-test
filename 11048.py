# 준규는 N, M 미로
# 각 방에는 사탕
# (1,1) -> (N,M)
# 방에 있는 사탕 다 가져갈 수 있다.
# 어캐가요~
# 토스 가는 사람들은 더 잘해용~

N, M = map(int, input().split())
MAP = []

for i in range(N):
    MAP.append(list(map(int, input().split())))

for n in range(N):
    for m in range(M):
        candi = [0]
        if (n - 1) >= 0:
            candi.append(MAP[n - 1][m])
        if (m - 1) >= 0:
            candi.append(MAP[n][m - 1])
        if (m - 1) >= 0 and (n - 1) >= 0:
            candi.append(MAP[n - 1][m - 1])
        MAP[n][m] += max(candi)
print(MAP[N-1][M-1])
