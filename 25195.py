from collections import deque

N, M = map(int, input().split())

edges = [[] for i in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)

S = int(input())

traps = list(map(int, input().split()))


# 쭉 가서 만나지 않고 마지막에 도착할 수 있다 = yes
# 무조건 만난다 = YES

def travel():
    global edges, traps, N

    if 1 in traps:
        return "Yes"
    Q = deque()
    Q.append(1)
    while Q:
        v = Q.pop()
        if len(edges[v]) == 0:
            return "yes"
        for w in edges[v]:
            if w not in traps:
                Q.append(w)
    return "Yes"


print(travel())
