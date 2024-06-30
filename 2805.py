# 나무 M미터
# H 지정 -> (나무길이 - H) 만큼의 나무가 생긴다.
# M미터 이상의 나무를 가져가야 한다.
# max(H)
import sys


def cut_trees(tree_array, height):
    total = 0
    for tree in tree_array:
        if tree < height:
            continue
        total += tree - height
    return total


def binary_search(array, target):
    low = 0
    high = array[-1]
    while low <= high:
        mid = (low + high) // 2
        cut_total = cut_trees(array, mid)
        if cut_total == target:
            return mid
        if cut_total > target:
            low = mid + 1
        if cut_total < target:
            high = mid - 1
    return high


_, M = map(int, input().split())
tree_line = sys.stdin.readline().rstrip()
trees = list(map(int, tree_line.split()))
trees.sort()
print(binary_search(trees, M))
