from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heappop(heap))
        except:
            print(0)
    else:
        heappush(heap, x)
