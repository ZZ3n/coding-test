# N
# M

N, M = map(int, input().split())
budgets = []
for i in range(N):
    budgets.append(int(input()))


def solve(array, depth, low, high):
    if low == high:
        return array[low]
    while low <= high:
        mid_value = sum(array[low:high + 1]) // 2
        mid = (low + high) // 2
        left = sum(array[:mid])
        right = sum(array[mid:])
        if left <= right:
            solve(array, depth + 1, left, mid)
            solve(array, depth + 1, mid, right)
        else:
            solve(array, depth + 1, left, mid)


def find_mid(array, low, high):
    mid_value = sum(array[low:high + 1]) // 2
    summ = 0
    for elem in range(low, high + 1):
        left = abs(sum(array[:elem]) - mid_value)
        right = abs(sum(array[elem:]) - mid_value)




print(budgets)
find_mid(budgets, 0, 6)
# solve(budgets, M, 0, N - 1)


'''
0x 100 1o 400 2x 300 3o 100 4x 500 5x 101 6x 400 

sum = 1901
mid_value = 950.5
left = 900      || right = 1001
100 400 300 100 || 500 101 400
1 1 v 20000

'''

'''
완전탐색으로 풀 수 있다.
0 1 2 3 4 
~
0 3 4 5 6 
까지 해서 결과 내기
'''
