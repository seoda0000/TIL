# import sys
# input = sys.stdin.readline
#
# N = int(input())
# skills = list(map(int, input().split()))
# hands = []
#
#
#
# for i in range(N):
#     k = N-1-i
#     if skills[k] == 1:
#         hands.insert(0, i+1)
#         ans = hands
#         hands = [i+1]
#
#     elif skills[k] == 2:
#         hands.insert(1, i+1)
#
#     else:
#         hands.append(i+1)
#
# print(*hands)

"""
61에서 시간초과
"""

import sys

input = sys.stdin.readline

N = int(input())
skills = list(map(int, input().split()))
hands = [0] * N
firstPoint = 0
secondPoint = 1
lastPoint = N - 1

for k in range(N):
    i = N - k

    if skills[k] == 1:
        hands[firstPoint] = i
        firstPoint = firstPoint + 1
        while firstPoint < lastPoint + 1 and hands[firstPoint] > 0:
            firstPoint += 1
        secondPoint = firstPoint + 1
        while secondPoint < lastPoint + 1 and hands[secondPoint] > 0:
            secondPoint += 1

    elif skills[k] == 2:
        hands[secondPoint] = i
        secondPoint += 1

    else:
        hands[lastPoint] = i
        lastPoint -= 1

print(*hands)
