# R, D
# R
# 순서 뒤집기
# D
# 첫번째 수 버리기
# 비어있을 때 하면 에러

from collections import deque


def arr_print(q: deque):
    print(f"[{','.join(list(map(str, q)))}]" )


def foo():
    operators = input()
    N = int(input())
    arr_string = input()[1:-1]
    if arr_string:
        arr = list(map(int, arr_string.split(",")))
    else:
        arr = []
    queue = deque(arr)
    isReverse = False
    for elem in operators:
        if elem == "R":
            isReverse = not isReverse
        else:
            if len(queue) == 0:
                print("error")
                return
            if isReverse:
                queue.pop()
            else:
                queue.popleft()

    if isReverse:
        queue.reverse()
    arr_print(queue)
    return


T = int(input())

result = []
for _ in range(T):
    foo()
