"""
https://www.acmicpc.net/problem/13567
백준 실버4 13567 로봇
"""

M, N = map(int, input().split())
orders = []
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
d = 2
ci = cj = 0
ans = True
for _ in range(N):
    order, num = input().split()
    orders.append((order, int(num)))

for order, num in orders:

    if order == 'MOVE':
        ni, nj = ci + di[d] * num, cj + dj[d] * num

        if not (0 <= ni < M and 0 <= nj < M):
            ans = False
            break

        ci, cj = ni, nj

    elif order == 'TURN':
        if num:
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

if ans:
    print(ci, cj)
else:
    print(-1)
