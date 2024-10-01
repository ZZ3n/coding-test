N, M = map(int, input().split())

jewels = []
for _ in range(M):
    jewels.append(int(input()))


def can(j):
    global jewels, N, M
    sum_p = 0
    for i in range(M):
        sum_p += jewels[i] // j
        if (jewels[i] % j) > 0:
            sum_p += 1
        if sum_p > N:
            return False
    return True


def foo():
    global jewels, N, M

    l = 1
    r = max(jewels)
    min_result = r
    while l < r:
        mid = (l + r) // 2
        if can(mid):
            r = mid - 1
            if mid < min_result:
                min_result = mid
        else:
            l = mid + 1
    return min_result


print(foo())
