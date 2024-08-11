# 두 용액 섞는다.
# 2 이상 100_000 이하

def mix(bottles, N):
    l = 0
    r = N - 1
    answer = [bottles[l], bottles[r]]

    while l < r:
        candi = [bottles[l], bottles[r]]
        sum_candi = sum(candi)

        if sum_candi == 0:
            return candi
        if abs(sum_candi) < abs(answer[0] + answer[1]):
            answer = [candi[0], candi[1]]
        if sum_candi > 0:
            r -= 1
        else:  # sum_candi < 0
            l += 1
    return answer


N = int(input())
bottles = list(map(int, input().split()))
bottles.sort()
result = mix(bottles, N)
print(result[0], result[1])
