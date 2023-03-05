"""
코딩테스트 연습
2023 KAKAO BLIND RECRUITMENT
미로 탈출 명령어
https://school.programmers.co.kr/learn/courses/30/lessons/150365
"""

from collections import defaultdict
from collections import deque

def solution(n, m, x, y, r, c, k):
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    answer = 'impossible'
    dic = defaultdict(int)
    stk = deque([(x, y, '')])

    while stk:
        i, j, w = stk.popleft()   # 좌표, 문자열
        t = len(w)                # 문자열 길이 : 여태까지 소모한 시간

        if t == k:                # k시간 소모시 continue
            if i == r and j == c:     # 목표지점 도착시 answer 반환
                answer = w
                break
            continue

        if k - t < abs(i - r) + abs(j - c):    # 남은 시간동안 목표지점에 가지 못할 경우 continue
            continue

        # 만약 t+1 시간만큼 소모했을 때 다음 지점에 이미 도착한 경우 continue (사전 순으로 더 빠른 루트가 이미 존재한다)
        # 그렇지 않은 경우 좌표와 t+1 시간을 기록 후 push

        if not dic[(i + 1, j, t + 1)] and i + 1 < n:
            dic[(i + 1, j, t + 1)] = 1
            stk.append((i + 1, j, w + 'd'))

        if not dic[(i, j - 1, t + 1)] and j - 1 >= 0:
            dic[(i, j - 1, t + 1)] = 1
            stk.append((i, j - 1, w + 'l'))

        if not dic[(i, j + 1, t + 1)] and j + 1 < m:
            dic[(i, j + 1, t + 1)] = 1
            stk.append((i, j + 1, w + 'r'))

        if not dic[(i - 1, j, t + 1)] and i - 1 >= 0:
            dic[(i - 1, j, t + 1)] = 1
            stk.append((i - 1, j, w + 'u'))

    return answer