L, N, K = map(int, input().split())
chargers = list(map(int, input().split()))


# 최소 거리 = 첫 충전소 까지
# 최대 거리 = L

def can_go(btr):
    # print(f"####### {btr} ######")
    global L, N, K, chargers
    now = btr
    result = 0
    pre_i = 0
    for i in chargers:
        if (i - pre_i) > btr:
            # print("CANT")
            return -1
        tmp = now - (i - pre_i)
        pre_i = i
        if tmp < 0:
            # print(tmp)
            result += 1
            now = btr
            # print(f"charge {pre_i} \t#p")
        if tmp == 0:
            result += 1
            now = btr
            # print(f"charge {i}")
        if tmp > 0:
            now = tmp
    if (L - chargers[-1]) > btr:
        return -1
    if now - (L - chargers[-1]) <= 0:
        result += 1
    return result


for i in range(L):
    times = can_go(i)
    if times <= K and times != -1:
        print(i)
        break
        # print(f"btr:{i}| times:{times}")
        # print("O ", end="")
