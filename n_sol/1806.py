N, S = map(int, input().split())

arr = list(map(int, input().split()))
dp = []
pre = 0

for i in range(N):
    sum_ = arr[i] + pre
    dp.append(sum_)
    pre = sum_
print(dp)

# b[5] - b[2] = 12
# = a[3] + a[4] + a[5]
# x ~ y 까지의 합
# dp[y] - dp[x-1]