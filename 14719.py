H, W = map(int, input().split())
wall_height = list(map(int, input().split()))

# 3 : [1, 2]
# 2 : [1, 2]
# 1 : [1]
result = 0
for h in range(H, 0, -1):
    pre_wall_idx = -1
    for w in range(W):
        # 자리에 벽이 없는 경우.
        if wall_height[w] < h:
            continue

        # 이전에 벽이 없었거나, 한 세트가 이미 생겨서 초기화된 경우.
        if pre_wall_idx == -1:
            pre_wall_idx = w
            continue
        # 벽이 붙어있는 경우
        if pre_wall_idx + 1 == w:
            pre_wall_idx = w
        else:
            result += w - (pre_wall_idx + 1)
            pre_wall_idx = w
print(result)


#_______O__
#___O___OO_
#_O_OO_OOOO