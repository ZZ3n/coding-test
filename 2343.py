# 총 N개의 강의가 있다.
# 순서를 유지해야 한다.
# 블루레이 디스크 개수가 M개이다.
# 블루레이 디스크 크기를 최대한 작게 해야한다.
import sys


def record(array, volume_limit):
    sum_vol = 0
    disk_cnt = 1
    for vol in array:
        if sum_vol + vol > volume_limit:
            disk_cnt += 1
            sum_vol = 0
        sum_vol += vol
    return disk_cnt


N, M = map(int, input().split())
lectures = list(map(int, sys.stdin.readline().split()))

s = max(lectures)
e = sum(lectures)

while s <= e:
    mid = (e + s) // 2

    cnt = record(lectures, mid)
    if cnt <= M:
        saved = mid
        e = mid - 1
    else:  # cnt > M
        s = mid + 1
print(saved)
"""
cnt가 계속 커서 saved가 안되지는 않는가?
=> cnt가 계속 크다? 
== 제한 크기가 너무 작다.
== 제한 크기를 늘리는데, 계속 M보다 크다. (s만 늘어남)
=> while문에서 결국 마지막 까지 온다면, 
=> s == e - 1 or s == e 이어야 한다.
=> 결국 mid는, s or e 로 정해진다.

=> 그 상황에도 cnt > M 이다? 
=> 답이 없는 문제이다
=> QED. 그럴 일 없다. 
"""