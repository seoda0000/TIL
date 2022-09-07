"""
트리의 기둥과 가지
https://www.acmicpc.net/problem/20924
골드4 20924

시청 공무원 마이크로는 과장으로부터 시에 있는 나무의 기둥의 길이와 가장 긴 가지의 길이를 파악하라는 업무 지시를 받았다.
마이크로는 ICPC Sinchon Winter Algorithm Camp에서 배운 트리 자료 구조를 이용하면 이 작업을 좀 더 수월하게 할 수 있으리라 판단했다.
마이크로는 트리의 기둥과 가지를 분류하기 위해 기가 노드를 추가로 정의하였다.
기가 노드는 루트 노드에서 순회를 시작했을 때, 처음으로 자식 노드가 $2$개 이상인 노드다. 기둥-가지를 줄여 기가 노드라 이름 붙였다.
마이크로는 시의 나무를 트리 자료 구조로 옮겼다. 그런데 과장이 마이크로에게 또 다른 업무를 지시했다! 너무 바쁜 마이크로를 대신해 트리의 기둥과 가장 긴 가지의 길이를 측정하자.
"""

import sys
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline().rstrip()


def dfs(x, cnt, findgiga):  # 해당 노드, 누적 길이, 기가 노드를 찾았는지 여부
    global giga, len_pillar, mxb
    visited[x] = True       # visited 기록

    # 1. 기가 노드 찾기
    if not findgiga:        # 만약 아직 기가 노드를 찾지 못했다면 (기둥이라면)
        if x == R and len(arr[x]) > 1:    # 루트 노드가 기가 노드인 경우 건너띄기
            pass
        elif x == R or len(arr[x]) == 2:  # 다른 노드와 연결된 경우
            for nxt in arr[x]:
                if not visited[nxt[0]]:       # 아직 방문하지 않은 노드라면 이동
                    dfs(nxt[0], cnt+nxt[1], False)  # 일방향이므로 clear가 필요 없다
        elif len(arr[x]) == 1:            # 기둥으로 끝날 경우
            len_pillar = cnt                        # 기둥 길이 계싼 후 종료
            return
        else:  # 기가 노드인 경우 기록
            giga = x
            len_pillar = cnt
            cnt = 0  # 이제 가지 길이를 구하기 위해 누적 길이 clear

    # 2. 최대 가지 길이 구하기
    if len(arr[x]) > 1:  # 다른 노드와 연결된 경우
        for a in arr[x]:
            nxt = a
            if not visited[nxt[0]]:  # 아직 방문하지 않은 노드라면 이동
                dfs(nxt[0], cnt+nxt[1], True)
    else:                # 가지의 끝인 경우
        if mxb < cnt:        # 최대 길이 갱신
            mxb = cnt
        return


N, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))


giga, len_pillar, mxb = R, 0, 0    # 기가노드, 기둥 길이, 최대 가지 길이
dfs(R, 0, False)
print(len_pillar, mxb)

