"""
https://www.acmicpc.net/problem/11727
백준 실버3 2×n 타일링 2
"""

N = int(input())
table = [0] * (N + 2)
table[1] = 1
table[2] = 3

for i in range(3, N + 1):
    table[i] = table[i - 2] * 2 + table[i - 1]

print(table[N] % 10007)
