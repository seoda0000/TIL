'''
빙고
https://www.acmicpc.net/problem/2578
백준 실버4 2578

빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다

다음은 사회자가 부르는 수를 차례로 지워나간다.

차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.

이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.

철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
'''


def b(arr):  # 빙고인지 확인하는 함수
    bingo = 0
    for a in arr:  # 행
        if a == [0, 0, 0, 0, 0]:
            bingo += 1
    for a in list(zip(*arr)):  # 열
        if a == (0, 0, 0, 0, 0):
            bingo += 1
    for n in range(5):  # 오른쪽 아래 대각선
        if arr[n][n] != 0:
            break
    else:
        bingo += 1
    for n in range(5):  # 왼쪽 위 대각선
        if arr[n][4 - n] != 0:
            break
    else:
        bingo += 1
    if bingo == 3:
        return True


arr = [list(map(int, input().split())) for _ in range(5)]
key = []
for _ in range(5):
    key += list(map(int, input().split()))

for z in range(11):  # 11회까지는 3 빙고 생성 불가
    k = key[z]
    for i in range(5):
        for j in range(5):
            if arr[i][j] == k:
                arr[i][j] = 0
f = True
for z in range(11, 25):  # 12회부터 3 빙고 여부 확인
    if f:
        k = key[z]
        for i in range(5):
            if f:
                for j in range(5):
                    if arr[i][j] == k:
                        arr[i][j] = 0
                        if b(arr):
                            print(z + 1)
                            f = False
                            break

"""
1년 후 코드
"""


def goBinggo(num):
    bingo = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:  # board에서 숫자 찾기
                v[i][j] = 1

                # 빙고인지 체크!
                # 1. 가로
                if sum(v[i]) == 5:
                    bingo += 1

                # 2. 세로
                if sum(list(zip(*v))[j]) == 5:
                    bingo += 1

                # 3. 오른쪽 아래 대각선
                if i == j:
                    cnt = 0
                    for a in range(5):
                        cnt += v[a][a]
                    if cnt == 5:
                        bingo += 1

                # 4. 왼쪽 위 대각선
                if i + j == 4:
                    cnt = 0
                    for a in range(5):
                        cnt += v[4 - a][a]
                    if cnt == 5:
                        bingo += 1
    return bingo


board = [input().split() for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(input().split())
v = [[0] * 5 for _ in range(5)]
ans = 0

for n in range(25):
    num = nums[n]
    ans += goBinggo(num)
    if ans >= 3:
        break

print(n + 1)

"""
count 개념 이용
"""


def goBinggo(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:  # board에서 숫자 찾기
                # 빙고인지 체크!
                # 1. 가로
                bingo[i] += 1

                # 2. 세로
                bingo[j + 5] += 1

                # 3. 오른쪽 아래 대각선
                if i == j:
                    bingo[10] += 1

                # 4. 왼쪽 위 대각선
                if i + j == 4:
                    bingo[11] += 1
    return


board = [input().split() for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(input().split())

bingo = [0] * 12

ans = 0

for n in range(25):
    num = nums[n]
    goBinggo(num)
    if bingo.count(5) >= 3:
        break

print(n + 1)
