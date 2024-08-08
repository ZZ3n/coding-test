# N
# 제각각의 랜선 K개
# 같은 길이의 랜선으로 만든다.
# N개보다 많아도 된다.

def cut(array, n, low, high):
    prev = 0
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            mid = 1
        sum_cnt = 0
        for line in array:
            sum_cnt += line // mid
        # print(f'low: {low}, mid: {mid}, high: {high}, sum_cnt: {sum_cnt}')
        if sum_cnt >= n:
            prev = mid
            low = mid + 1
        else:  # sum_cnt < n
            high = mid - 1
    return prev


K, N = map(int, input().split())
lines = []
for i in range(K):
    lines.append(int(input()))
R = cut(lines, N, 0, sum(lines) // N)
print(R)
