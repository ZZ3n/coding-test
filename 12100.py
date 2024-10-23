N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

def copy_mat(ori):
    global N
    dest = []
    for i in range(N):
        dest.append([])
        for j in range(N):
            dest[i].append(ori[i][j])
    return dest


def slide(matrix, dx, dy):
    global N
    # dx = 1 => N-1 ~ 0
    mat = copy_mat(matrix)
    for k in range(N):
        if dx > 0:
            sx = N - 1
        elif dx < 0:
            sx = 0
        else:
            sx = k

        if dy > 0:
            sy = N - 1
        elif dy < 0:
            sy = 0
        else:
            sy = k
        # print(f"s= ({sx}, {sy})")
        for i in range(N):
            # 0 1 2 3 ...
            nx = sx - dx * i
            ny = sy - dy * i
            # print(f"n : ({sx}, {sy})")

            for j in range(i + 1, N):
                tx = sx - dx * j
                ty = sy - dy * j
                
                # 타겟이 0 인 경우는 
                if mat[ty][tx] == 0:
                    continue

                # 자신이 0 인 경우 땡겨옴
                if mat[ny][nx] == 0:
                    mat[ny][nx] = mat[ty][tx]
                    mat[ty][tx] = 0
                    continue
                # ny, nx 는 0 인 경우 없음.
                # n=v, t=v
                ## 합칠 수 있는 경우.
                if mat[ny][nx] == mat[ty][tx]:
                    mat[ny][nx] += mat[ty][tx]
                    mat[ty][tx] = 0
                if mat[ny][nx] != mat[ty][tx]:
                    break
    max_ = 0
    for i in range(N):
        max_ = max(max_, max(mat[i]))
    return mat, max_


def brute_force():
    global M
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    matrixs = [[] for _ in range(6)]
    matrixs[0] = [M]
    answer = 0
    for j in range(5):
        for k in range(len(matrixs[j])):
            for i in range(4):
                mat, maxi = slide(matrixs[j][k], d[i][0], d[i][1])
                matrixs[j + 1].append(mat)
                if maxi > answer:
                    answer = maxi
    print(answer)
brute_force()