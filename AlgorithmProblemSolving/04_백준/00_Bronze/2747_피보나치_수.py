"""
https://www.acmicpc.net/problem/2747
백준 브론즈2 2747 피보나치 수

"""
N = int(input())
fibo = [0] * (N + 1)
fibo[1] = 1

for i in range(2, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
print(fibo[N])
