N = int(input())

# 한번에 정리하나, 힙에 정리하나 똑같나?

numbers = list(map(int, input().split()))
numbers.sort()


def is_good(target_idx):
    global numbers, N

    if N < 3:
        return False

    l = 0
    r = N - 1

    while l < r:
        if l == target_idx:
            l += 1
            continue
        if r == target_idx:
            r -= 1
            continue
        left = numbers[l]
        right = numbers[r]
        candidate = left + right

        if candidate == numbers[target_idx]:
            # print(f"n[{l}] + n[{r}] = {numbers[l]} + {numbers[r]} = n[{target_idx}] = {numbers[target_idx]}")
            return True
        if candidate < numbers[target_idx]:
            l += 1
        else:  # candidate > numbers[target_idx]:
            r -= 1
    return False


result = 0
for i in range(N):
    if is_good(i):
        result += 1
print(result)
