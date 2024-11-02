import sys


N = int(input())
# ops = {"add": 0, "remove": 1, "check": 2, "toggle": 3, "all": 4, "empty": 5}
S = set()

for i in range(N):
    lane = list(sys.stdin.readline().strip().split())

    op = lane[0]
    if len(lane) == 1:
        if op[0] == "a":
            S = set(list(range(1, 21)))
        else:  # empty
            S.clear()
        continue
    elem = int(lane[1])

    if op[0] == "r":
        S.discard(elem)
    elif op[0] == "c":
        print(1 if elem in S else 0)
    elif op[0] == "t":
        if elem in S:
            S.discard(elem)
        else:
            S.add(elem)
    elif op[0] == "a":
        S.add(elem)
