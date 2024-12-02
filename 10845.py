from collections import deque

T = int(input())
Q = deque()
for _ in range(T):

    op, *others = input().split()
    print(others)
    if op == "push":
        Q.append(int(others[0]))
    elif op == "pop":
        Q.pop(int(others[0]))
    elif op == "size":
        len(Q)
    elif op == "empty":
        pass
    elif op == "front":
        pass
    elif op == "back":
        pass
