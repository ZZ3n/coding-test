N, K = map(int, input().split())
dp = [[0 for __ in range(N)] for _ in range(K + 1)]
goods = []
for i in range(N):
    w, v = map(int, input().split())
    goods.append((w, v))
goods.sort()

"""
Solve(W, 1~5) = max( Solve(W - w1, 2~5) + v1, Solve(W, 2~5) )
dp[N-1][W] = max( dp[N-2][W-w1] + v1, dp[N-2][W] )
"""

for w_limit in range(1, K + 1):
    for i in range(N):
        w, v = goods[i]
        if i == 0:
            if w <= w_limit:
                dp[w_limit][i] = v
            else:
                dp[w_limit][i] = 0
            continue
        if w <= w_limit:  # 넣을 수 있는 경우.
            # max(넣는 경우, 안 넣는 경우)
            dp[w_limit][i] = max(dp[w_limit - w][i - 1] + v, dp[w_limit][i - 1], )
        else:
            dp[w_limit][i] = dp[w_limit][i - 1]
print(dp[K][N-1])