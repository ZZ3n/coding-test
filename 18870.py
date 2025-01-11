N = int(input())

positions = list(map(int, input().split()))

sorted_pos = positions.copy()
sorted_pos.sort()
result = {}
pre = -(10**10)
cnt = 0
for pos in sorted_pos:
    if pre == pos:
        continue
    else:  # pre < pos
        pre = pos
        result[pos] = cnt
        cnt += 1


for pos in positions:
    print(result[pos], end=" ")
