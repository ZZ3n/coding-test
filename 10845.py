from collections import deque

T = int(input())
Q = deque()
for _ in range(T):

    op, *others = input().split()
    # print(op,others)
    # print(others)
    if op == "push":
        Q.append(int(others[0]))
    elif op == "size":
        print(len(Q))

    elif op == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif len(Q) == 0:
        print(-1)
    else:
        if op == "pop":
            print(Q.popleft())
        elif op == "front":
            print(Q[0])
        elif op == "back":
            print(Q[-1])
