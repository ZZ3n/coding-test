from collections import deque

def solution(bridge_length, weight, truck_weights):
    W = 0
    T = 1
    w_q = deque(truck_weights)
    
    n_q = deque()
    n_w = 0
    
    cnt = 0
    while w_q or n_q:
        # 다리 탈출
        while n_q:
            # 맨 앞차의 위치 체크
            if cnt - n_q[0][T] < bridge_length: 
                break
            # 맨 앞차가 나갔다면, 나간 처리
            w, t = n_q.popleft() 
            # print(f"{cnt}s out >> {w}w {t}s")
            n_w -= w
            
        # 다리 진입
        if w_q:
            # 다리에 차가 꽉 찬 경우, 다리 무게가 안되는 경우
            if len(n_q) < bridge_length and w_q[0] + n_w <= weight:
                truck = w_q.popleft()
                # print(f"{cnt}s in  >> {truck}w {cnt}s")
                n_q.append((truck, cnt))
                n_w += truck
        cnt += 1
        # print(n_q)
    
            
    return cnt