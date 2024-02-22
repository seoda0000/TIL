"""
https://www.acmicpc.net/problem/10830
백준 골드4 행렬 제곱
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오.
수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
"""


def cal(a, b):  # 행렬 a와 b의 행렬곱
    ab = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            val = 0
            for n in range(N):
                val += a[i][n] * b[n][j]
            ab[i][j] = val % 1000
    return ab


def get_answer(arr, b):  # arr의 b 제곱 구하기
    if b == 1:
        result = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                result
        return arr
    else:
        half = get_answer(arr, b // 2)
        result = cal(half, half)
        if b % 2:
            return cal(result, arr)
        else:
            return result


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        arr[i][j] %= 1000
ans = get_answer(arr, B)
for a in ans:
    print(*a)
