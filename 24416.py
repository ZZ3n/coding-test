def fib(n):
    if n == 1 or n == 2:
        return 1, 1
    else:
        a, cntA = fib(n - 1)
        b, cntB = fib(n - 2)
        return a + b, cntA + cntB


def fibonacci(n):
    cnt = 0
    f = [0, 1, 1]
    for i in range(3, n + 1):
        cnt += 1
        f.append(f[i - 1] + f[i - 2])
    return f[n], cnt


n = int(input())
fa, a = fib(n)
fb, b = fibonacci(n)

print(a, b)
