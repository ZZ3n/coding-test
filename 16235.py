from collections import deque

N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

mat = [[5] * N for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    dead_trees = []
    for i in range(N):
        for j in range(N):
            len_ = len(trees[i][j])
            for k in range(len_):
                if mat[i][j] < trees[i][j][k]:
                    for _ in range(k, len_):
                        dead_trees.append([trees[i][j].pop(), i, j])
                    break
                else:
                    mat[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for age, x, y in dead_trees:
        mat[x][y] += age // 2

    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for t in range(8):
                        nx = i + dx[t]
                        ny = j + dy[t]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        trees[nx][ny].appendleft(1)
            mat[i][j] += A[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])
print(answer)
