"""
메모리 초과 코드
"""


def chooseNumber(all, cnt, nth) -> None:  # all개의 숫자 중 cnt개의 숫자 뽑기

    if cnt == nth:
        numbers.append(tuple(number))
        return

    if nth == 0:
        s = -1
    else:
        s = number[-1]

    for a in range(s + 1, all):
        if a not in number:
            number.append(a)
            chooseNumber(all, cnt, nth + 1)
            number.pop()


def findSequenceGroup(n) -> list:  # 요소 n개를 뺀 부분 수열 리스트 반환
    group = []

    chooseNumber(lenW1, n, 0)

    for number in numbers:
        g = []
        for a in range(lenW1):
            if a not in number:
                g.append(word1[a])
        group.append(tuple(g))
    return list(set(group))


def isSubSequence(w: str, l: list) -> bool:  # 문자 수열 l이 문자열 w 안에 있는지 확인

    lastIdx = -1
    p = 0
    while lastIdx < len(w) and p < len(l):
        if w[lastIdx + 1:].find(l[p]) == -1:
            return False
        elif lastIdx + 1 < len(w):
            lastIdx += 1 + w[lastIdx + 1:].index(l[p])
            p += 1

    return True


word1 = input()
word2 = input()
if len(word1) > len(word2):
    word1, word2 = word2, word1
lenW1 = len(word1)
lenW2 = len(word2)
flag = 0
for n in range(lenW1):
    # lenW1 - n: 찾을 수열 길이
    # n: 뺄 단어 개수
    number = []
    numbers = []
    lst = findSequenceGroup(n)  # 길이에 해당하는 문자 수열 리스트

    for l in lst:
        if isSubSequence(word2, l):
            print(lenW1 - n)
            flag = 1
            break
    if flag:
        break
"""
자체 DP 적용 코드 : 시간 초과
"""

word1 = input().strip()
word2 = input().strip()

arr = [0] * len(word2)

for a in range(len(word1)):
    now = word1[a]
    for b in range(len(word2))[::-1]:
        if word2[b] == now:
            if a == 0 or b == 0:
                arr[b] = 1
            else:
                arr[b] = max(arr[:b]) + 1
ans = max(arr)
print(ans)

"""
LCS DP 적용 코드

dp를 쓸 때는 한 칸 한 칸의 의미에 집중 하자. 행과 열이 만나는 지점이 칸이다!!
"""
import sys

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

arr = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

for a in range(1, len(word1) + 1):
    now = word1[a - 1]
    for b in range(1, len(word2) + 1):
        here = word2[b - 1]
        if word2[b - 1] == now:
            arr[b][a] = arr[b - 1][a - 1] + 1
        else:
            arr[b][a] = max(arr[b][a - 1], arr[b - 1][a])

print(arr[-1][-1])
