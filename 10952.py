flag = True
while flag:
    a, b = map(int, input().split())
    if a == 0:
        break
    print(a + b)