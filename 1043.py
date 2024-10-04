# 1. truth 가 있으면, truth는 전염된다.

N, M = map(int, input().split())
truth_n = list(map(int, input().split()))[1:]
parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

know_truth = [False for _ in range(N + 1)]
for t in truth_n:
    know_truth[t] = True
    # print(f"already know : {t}")

know_truth_p = [False for _ in range(M)]

changed = True
while changed:
    changed = False
    for i in range(M):
        if know_truth_p[i]:
            continue
        for p in parties[i]:
            if know_truth[p]:
                for pa in parties[i]:
                    # print(f"now know : {pa}")
                    know_truth[pa] = True
                # print(f"party know : {i}")
                know_truth_p[i] = True
                changed = True

                break
sum_liar = 0
for m in range(M):
    if know_truth_p[m]:
        sum_liar += 1
print(M-sum_liar)