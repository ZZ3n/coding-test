N, M = map(int, input().split())

l = set()
m = set()

for _ in range(N):
    l.add(input())

for _ in range(M):
    m.add(input())

result = list(l & m)

result.sort()

print(len(result))
for r in result:
    print(r)
