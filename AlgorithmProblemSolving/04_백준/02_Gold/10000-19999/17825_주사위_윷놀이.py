"""
실행시간: 280 -> 456
풀이시간: 62분 -> 20분

인덱스 오류를 빨리 찾았다. 점수를 인덱스로 헷갈렸다.
이전엔 모든 말이 도착했을 경우에 ans를 갱신해주었는데, 이번엔 그냥 모든 상황에서 갱신해주었다.
또한 보드판의 상황을 나타내는 board 변수를 아예 없애고 말들의 현재 위치 인덱스 배열만을 사용했다.

시간은 오래 걸리지만 코드는 짧아졌다.
"""

"""
2:20 시작
2:27 구상완료
2:37 디버깅 - 인덱스 오류
2:40 제출

"""


def move(cur, dice):
    if cur in blue.keys():  # 파란 칸
        cur = blue[cur]
        dice -= 1
    for _ in range(dice):
        cur = nxt[cur]

    if cur != 21 and cur in horses:
        cur = -1
    return cur


def dfs(turn, sm):
    global ans

    ans = max(ans, sm)
    if turn == 10:
        return

    for x in range(4):
        cur = horses[x]
        if cur == 21:
            continue
        done = False
        nxt = move(cur, dice_lst[turn])
        if nxt >= 0:
            horses[x] = nxt
            dfs(turn + 1, sm + score[nxt])
            horses[x] = cur

    return


score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0,
         13, 16, 19, 25, 30, 35,
         22, 24,
         28, 27, 26]
nxt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
       12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21,
       23, 24, 25, 26, 27, 20,
       29, 25,
       31, 32, 25]
blue = {5: 22, 10: 28, 15: 30}
horses = [0] * 4
dice_lst = list(map(int, input().split()))
ans = 0
dfs(0, 0)
print(ans)

"""

2:45 시작
3:38 1차 구현 완료
3:47 디버깅 완료

<실수한 부분>
눈이 침침허다

틀렸습니다가 뜨고 로직에서 오류를 찾을 수 없어서 룩업 테이블을 하나하나 봤다.
역시나 27을 21로 잘못 보고 29를 28로 잘못 봤다... 진짜냐...
상수를 그대로 넣는 룩업 테이블은 꼼꼼하게 검토해야겠다
또박또박 쓰자
"""


def dfs(nth, s):
    global ans
    if nth == 10:  # 10턴 완료
        ans = max(ans, s)
        return

    # 주사위 굴리기
    dice = dice_lst[nth]

    # 말 선택하기
    all_horses_arrived = True
    for h in range(1, 5):
        start = cur_horses[h]  # 시작점
        cur = start
        if cur == 32:  # 이미 도착한 말: pass
            continue

        all_horses_arrived = False  # 아직 움직일 말이 있다

        # 파란 칸에서 시작해서 이동
        if cur in blue_set:
            cur = blue_dic[cur]
            for _ in range(dice - 1):
                cur = nxt[cur]

        # 이외 칸에서 시작해서 이동
        else:
            for _ in range(dice):
                cur = nxt[cur]

        # 도착점이 아니고, 이미 다른 말이 있다면 불가능
        if board[cur] and cur != 32:
            continue
        else:
            cur_horses[h] = cur  # check
            board[cur] = h
            board[start] = 0

            dfs(nth + 1, s + scores[cur])  # 다음 턴

            cur_horses[h] = start  # clear
            board[cur] = 0
            board[start] = h

    if all_horses_arrived:  # 모든 말이 이미 도착 -> 종료
        ans = max(ans, s)
        return


dice_lst = list(map(int, input().split()))

scores = [0,
          2, 4, 6, 8, 10,
          12, 14, 16, 18, 20,
          22, 24, 26, 28, 30,
          32, 34, 36, 38, 40,
          13, 16, 19, 25, 30,
          35, 22, 24, 28, 27,
          26, 0]  # i번째 칸의 점수

nxt = list(range(1, 21)) \
      + [32, 22, 23, 24, 25, 26, 20] \
      + [28, 24, 30, 31, 24, 32]  # i번째 칸의 다음 칸

blue_dic = {5: 21, 10: 27, 15: 29}  # 파란 칸의 다음 칸
blue_set = {5, 10, 15}  # 파란 칸

cur_horses = [0] * 5  # i번째 말의 현재 위치
board = [0] * 33  # 보드 상황 (0: 빈칸, 1~4: 말)

ans = 0
dfs(0, 0)
print(ans)
