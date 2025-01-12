from collections import deque

N = int(input())

MAP = []

for i in range(N):
    lane = list(map(int, input().split()))
    MAP.append(lane)

MIX = -1
BLUE = 1
WHITE = 0

def check_color(sx, sy, l):
    first_color = MAP[sy][sx]
    for x in range(sx, sx + l):
        for y in range(sy, sy + l):
            if MAP[y][x] != first_color:
                return MIX

    return first_color


Q = deque()
Q.append((0, 0, N))

white_cnt = 0
blue_cnt = 0
while Q:
    x, y, l = Q.popleft()
    color_on_sq = check_color(x, y, l)
    if color_on_sq == WHITE:
        white_cnt += 1
    elif color_on_sq == BLUE:
        blue_cnt += 1
    else:
        nl = l // 2
        nx = x + nl
        ny = y + nl

        Q.append((x, y, nl))
        Q.append((nx, y, nl))
        Q.append((x, ny, nl))
        Q.append((nx, ny, nl))

print(white_cnt)
print(blue_cnt)