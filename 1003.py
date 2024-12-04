T = int(input())

fibo = [[-1, -1] for i in range(41)]  # 0, 1~40
fibo[0] = [1, 0]
fibo[1] = [0, 1]
fibo[2] = [1, 1]
fibo[3] = [1, 2]
# fibo[5] = fibo[4] + fibo[3]


def get_fibo(n):
    if fibo[n][0] == -1:
        result_1 = get_fibo(n - 1)
        result_2 = get_fibo(n - 2)
        fibo[n][0] = result_1[0] + result_2[0]
        fibo[n][1] = result_1[1] + result_2[1]
    return fibo[n]


for t in range(T):
    result = get_fibo(int(input()))
    print(result[0], result[1])
