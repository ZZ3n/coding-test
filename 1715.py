from queue import PriorityQueue
N = int(input())
Q = PriorityQueue()
for i in range(N):
    Q.put(int(input()))
cnt = 0
while Q.queue:
    a = Q.get()
    if Q.empty():
        break
    b = Q.get()
    cnt += a + b
    Q.put(a + b)
print(cnt)