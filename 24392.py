N, M = map(int, input().split())
MAP = []
MEM = [[0 for _ in range(M)] for __ in range(N)]
for i in range(N):
    MAP.append(list(map(int, input().split())))

for i in range(M):
    MEM[0][i] = MAP[0][i]

for n in range(1, N):
    for m in range(M):
        if MAP[n][m] == 0:
            continue
        summ = 0
        if (m - 1) >= 0:
            summ += MEM[n - 1][m - 1]
        summ += MEM[n - 1][m]
        if (m + 1) < M:
            summ += MEM[n - 1][m + 1]
        MEM[n][m] = summ
print(sum(MEM[-1])%1_000_000_007)
