"""
1 => 1
1

2 => 2
2
1+1 

3 => 4
3
1+2 2+1
1+1+1

4 => 7
1+3 2+2 3+1
2+1+1 1+2+1 1+1+2 
1+1+1+1

5 => 13
2+3 3+2 
3+1+1 1+3+1 1+1+3 2+2+1 2+1+2 1+2+2
2+1+1+1 1+2+1+1 1+1+2+1 1+1+1+2
1+1+1+1+1
"""

T = int(input())
dp = [0 for i in range(15)]


def get_dp(i):
    global dp
    if dp[i] != 0:
        return dp[i]
    dp[i] = get_dp(i - 1) + get_dp(i - 2) + get_dp(i - 3)
    return dp[i]


dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for t in range(T):
    n = int(input())
    print(get_dp(n))
