N = 10
total = 0
for i in range(N):
    s = int(input())
    if abs(100 - total) >= abs(100 - (total + s)):
        total += s
    else:
        break
print(total)
