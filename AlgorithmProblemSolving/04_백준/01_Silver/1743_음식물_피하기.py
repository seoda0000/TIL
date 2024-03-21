"""
https://www.acmicpc.net/problem/1743

백준 실버1 1743 음식물 피하기

코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.

이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다.

통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.
"""


def check(i, j):
    cnt = 0
    v[i][j] = 1
    q = [(i, j)]
    while q:
        cnt += 1
        ci, cj = q.pop(0)
        for n in range(4):
            ni, nj = ci + di[n], cj + dj[n]
            if v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
            v[ni][nj] = 1

    return cnt


N, M, K = map(int, input().split())
arr = [[0] * (M + 2) for _ in range(N + 2)]
v = [[0] * (M + 2) for _ in range(N + 2)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
ans = 0

for _ in range(K):  # 음식물 표시하기
    a, b = map(int, input().split())
    arr[a][b] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if v[i][j] == 0 and arr[i][j] == 1:

            ans = max(ans, check(i, j))  # 음식물 크기 구하기

        else:
            v[i][j] = 1

print(ans)
