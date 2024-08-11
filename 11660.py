# x1,y1 ~ x2,y2 까지의 합을 구하시오.

N, M = map(int, input().split())

matrix = []
prefix_sum = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
result = []

for i in range(N):
    matrix.append(list(map(int, input().split(" "))))

for y in range(1, N + 1):
    for x in range(1, N + 1):
        prefix_sum[y][x] = (
                matrix[y - 1][x - 1]
                + prefix_sum[y - 1][x]
                + prefix_sum[y][x - 1]
                - prefix_sum[y - 1][x - 1]
        )


for i in range(M):
    x1, y1, x2, y2 = map(int, input().split(" "))
    result.append(prefix_sum[x2][y2] +prefix_sum[x1 - 1][y1 - 1] -prefix_sum[x1 - 1][y2] -prefix_sum[x2][y1 - 1])

for r in result:
    print(r)
