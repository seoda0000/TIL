"""
실행시간: 128(124) -> 120
풀이시간: 60분 -> 22분

코드트리와 백준이 x, y가 반대라 틀렸다. 황당...하지만 앞으로는 확인하자.
소현 프로님 풀이를 적용해서 우선 방향리스트를 구한 후에 한번에 찍었다. 빠르다!
시계 + 반대방향 -> 반시계라는 사실을 숙지하자.

배열에 표시하는 문제는 규칙부터 찾은 이후에 그리면 심플해진다.
"""

"""
14:00 시작
14:04 구상 완료
14:11 구현 완료
14:15 제출
14:22 백준 제출
"""


def get_dlst(d, g):
    dlst = [d]

    for _ in range(g):
        nd = len(dlst)

        for x in range(nd)[::-1]:
            dlst.append((dlst[x] + 1) % 4)

    return dlst


def draw(arr, x, y, dlst):
    ci, cj = x, y
    arr[ci][cj] = 1
    for d in dlst:
        ci, cj = ci + di[d], cj + dj[d]
        arr[ci][cj] = 1
    return


di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dlst = get_dlst(d, g)
    draw(arr, x, y, dlst)
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            ans += 1
print(ans)

"""
9:07~9:33 구상
9:34 구현 시작

10:07 구현 완료


옆분이 이 문제 플래티넘이라고 해서 쫄아서 엄청 천천히 풀었다...(아니잖아요)
문제 자체가 이해가 안되어서 그래프를 네번이나 그렸다. 겨우 이해했다.
규칙을 단계별로 찾고 구현했다. 함수 구조를 안 짜고 구현에 들어가서 잠시 헤맸다...
재귀는 꼭 함수 구조를 잡고 들어가자.

문제 자체에서 그래프를 이상하게 줘서 헤맸는데, 생각해보니 xy가 아닌 ij로 생각하면 그대로 풀어도 된다! 이걸 좀 늦게 깨달았다.
최근 푼 문제가 위아래를 뒤집는 문제라서 같은 유형인줄 알고 착각했다가, 그럴 필요가 없다는 걸 깨닫고 중간에 방향을 다 반대로 바꿨다.
심지어 xy를 ji로 받아야 했는데 그걸 놓쳐서 디버깅이 길어졌다.

그래프 문제는 방향부터 잡고 가자...

반대+시계돌리기 -> 반시계 돌리기로 개선
"""

import sys

input = sys.stdin.readline


# 이번 세대 그린 후 (이번 세대 끝점, 여태까지의 방향 리스트 반환)
def get_direction(g):  # g: 세대 정보

    if g == 0:
        arr[si][sj] |= 1
        ni, nj = si + di[sd], sj + dj[sd]
        arr[ni][nj] |= 1
        return ni, nj, [sd]

    else:
        ci, cj, ddlst = get_direction(g - 1)  # 이번 세대 시작 위치, 지난 방향들

        cdlst = []  # 이번 세대 방향 리스트
        for dd in ddlst[::-1]:  # 역순으로 반시계 돌리기 수행
            cdlst.append(((dd + 1) % 4))

        # 드래곤 커브 그리기
        for dd in cdlst:
            ni, nj = ci + di[dd], cj + dj[dd]
            arr[ni][nj] |= 1
            ci, cj = ni, nj

        return ci, cj, ddlst + cdlst


di = [0, -1, 0, 1]  # 0:오른쪽, 1:위쪽, 2:왼쪽, 3: 아래쪽
dj = [1, 0, -1, 0]
N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
arr = [[0] * 101 for _ in range(101)]

for curve in curves:
    sj, si, sd, g = curve
    get_direction(g)

ans = 0
for i in range(100):  # 왼쪽 아래 꼭지점 기준으로 칸 세기
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            ans += 1

print(ans)
