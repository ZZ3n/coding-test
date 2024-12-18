"""
0~3 , 4~7
8~11, 12~15


4행 5열 -> 49

(4,5) -> (2,2+1)

8*8 일때,
4*4 * 4이다.
0~15 16~31
32~47 47~63

n일때,
(r,c)의 사분면상 위치를 잡는다.
계속해서 잡는다.

"""

"""
1 2
3 4
"""


def which_quadrants(M, x, y):
    result = 0
    result += 0 if x < M // 2 else 2
    result += 0 if y < M // 2 else 1

    return result


N, R, C = map(int, input().split())

n = N
r = R
c = C
result = 0
for _ in range(N):
    quadrant = which_quadrants(2**n, r, c)
    result += (2**n * 2**n) // 4 * quadrant
    if r >= 2 ** (n - 1):
        r = r % 2 ** (n - 1)
    if c >= 2 ** (n - 1):
        c = c % 2 ** (n - 1)
    n -= 1
print(result)
