while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    maxi = max(a, b, c)
    if maxi == a:
        if (a**2 == b**2 + c**2):
            print("right")
            continue
    if maxi == b:
        if (b**2 == a**2 + c**2):
            print("right")
            continue
    if maxi == c:
        if (c**2 == a**2 + b**2):
            print("right")
            continue
    print("wrong")
