"""
15:18 문제 읽기 시작
16:06 구현 완료

심신이 미약한 상태로 풀기 시작해서 상당히 더럽다...
경우를 나눠 각각의 상황마다 구상을 했다.
이전 위치를 돌아보지 않겠다고 생각하고 갔는데, 오르락 내리락거리는 부분 때문에 v 배열을 적용해서 풀었다.
v 배열을 적용하면 이전에 썼던 변수를 상당량 지워도 돌아간다.

transpose를 싫어해서 안 썼는데... 단순 행 열 순회면 적극적으로 쓰도록 해봐야겠다. 훨씬 깔끔해진다!
구상을 조금 더 꼼꼼히 하자
"""


def check(ci, cj):
    global cnt

    if cj >= N - 1:
        cnt += 1
        return

    ck = arr[ci][cj]
    nk = arr[ci][cj + 1]

    if nk > ck + 1:
        return

    elif nk == ck + 1:
        for x in range(cj - L + 1, cj + 1):
            if x < 0: return
            if arr[ci][x] != arr[ci][cj]: return
            if v[x]:
                return
            else:
                v[x] = 1
        check(ci, cj + 1)

    elif nk == ck:
        check(ci, cj + 1)

    elif nk == ck - 1:
        for x in range(cj + 1, cj + 1 + L):
            if x >= N: return
            if arr[ci][x] != arr[ci][cj + 1]: return
            if v[x]:
                return
            else:
                v[x] = 1
        check(ci, cj + L)

    else:
        return

    return


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):  # 행 확인
    v = [0] * N
    check(i, 0)
arr = list(zip(*arr))
for i in range(N):  # 열 확인
    v = [0] * N
    check(i, 0)

print(cnt)
