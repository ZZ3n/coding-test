N, S = map(int, input().split())

arr = list(map(int, input().split()))
dp = []
pre = 0

s = 0
r = 0
answer = 100001
for l in range(N):
    while s < S and r < N:
        s += arr[r]
        r += 1
    if s >= S:
        answer = min(answer, r - l)
    s -= arr[l]

if answer == 100_001:
    print(0)
else:
    print(answer)

# 부분합 + 투포인터 이용해서 풀기

# b[5] - b[2] = 12
# = a[3] + a[4] + a[5]
# x ~ y 까지의 합
# dp[y] - dp[x-1]
