import sys


def binary_search(array, low, high, budget):
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for city in array:
            if city > mid:
                total += mid
            else:
                total += city
        if total == budget:
            return mid
        elif total > budget:
            high = mid - 1
        else:
            low = mid + 1
    return high  # or low


N = int(input())
cities = list(map(int, sys.stdin.readline().split()))
money = int(input())
print(binary_search(cities, 0, max(cities), money))
