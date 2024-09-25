N = int(input())

nums = list(map(int, input().split()))
nums.sort()

result = 0


def find(idx, arr):
    l = 0
    r = len(arr) - 1
    if len(arr) <= 2:
        return False
    target = arr[idx]
    while l < r:
        temp = arr[l] + arr[r]
        if temp == target:
            # print(f"O :{target} || {l} < {target} < {r}")
            return True
        if temp > target:
            r = r - 1
            if r == idx:
                r = r - 1
        else:  # temp < target:
            l = l + 1
            if l == idx:
                l = l - 1
    # print(f"X :{target}")
    return False


for i in range(N):
    if find(i, nums):
        result += 1
print(result)
