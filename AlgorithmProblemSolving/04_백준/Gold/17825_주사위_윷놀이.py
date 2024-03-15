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
