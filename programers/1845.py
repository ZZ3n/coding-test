"""
N마리 제시, N/2마리 선택
최대한 많은 종류의 폰켓몬
"""

def solution(nums):
    ponketmons = set(nums)
    maxi = len(ponketmons)
    if len(nums) // 2 < maxi:
        return len(nums) // 2
    return maxi

