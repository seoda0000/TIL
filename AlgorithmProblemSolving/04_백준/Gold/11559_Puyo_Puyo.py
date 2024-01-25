"""
https://www.acmicpc.net/problem/11559

뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다.
이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다.
하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

"""


def check(i, j, color):  # 뿌요가 터졌는지 check
    v[i][j] = 1
    buyos = [(i, j)]
    cnt = 0
    while cnt < len(buyos):  # 모여 있는 뿌요 찾기
        ci, cj = buyos[cnt]
        cnt += 1
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if v[ni][nj] == 0:
                if arr[ni][nj] == color:
                    buyos.append((ni, nj))
                elif arr[ni][nj] != '.':  # 다른 색상 뿌요면 skip (v 표시 x)
                    continue
                v[ni][nj] = 1

    if cnt >= 4:  # 4개 이상 모였으면 팡
        for buyo in buyos:
            ci, cj = buyo
            arr[ci][cj] = '.'
        return True
    else:
        return False


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
arr = [['.'] + list(input()) + ['.'] for _ in range(12)]
arr.insert(0, ['.'] * 8)
arr.append(['.'] * 8)

ans = 0

while True:

    v = [[0] * 8 for _ in range(14)]
    temp = 0
    for i in range(1, 13):
        for j in range(1, 7):
            if v[i][j] == 0 and arr[i][j] != '.':
                if check(i, j, arr[i][j]):
                    temp += 1
            else:
                v[i][j] = 1
    if temp == 0:  # 아무것도 안 터졌을 경우
        break
    else:  # 터졌을 경우 아래로 drop
        ans += 1

        for j in range(1, 7):
            blank = 0
            for i in range(1, 13)[::-1]:
                if arr[i][j] == '.':
                    blank += 1
                else:
                    if blank > 0:
                        arr[i + blank][j] = arr[i][j]
                        arr[i][j] = '.'

print(ans)
