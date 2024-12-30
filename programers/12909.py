from collections import deque

def solution(s):
    answer = True
    
    arr = list(s)
    Q = deque()
    for c in arr:
        
        if c == "(":
            Q.append(c)
        else:
            try:
                Q.pop()
            except IndexError:
                return False

    return False if Q else True