import sys

input = sys.stdin.readline


def choose_player(nth):  # nth번째 채워서 가능한 모든 순열 얻기
    if nth == 10:  # 순열이 완성되면 게임 시작
        play_game()
        return
    if nth == 4:
        choose_player(5)
    else:
        for i in range(2, 10):
            if i in numbers:
                continue
            numbers[nth] = i
            choose_player(nth + 1)
            numbers[nth] = 0
    return


def play_game():  # 시뮬레이션 돌려서 최대 점수 갱신
    global mx

    output = 0
    p = 1  # 1번 타자부터 시작
    for n in range(N):
        if (N - n) * 24 + output <= mx:  # 가지치기
            return
        board = []  # 3 아웃 전 결과 기록
        scores = players[n]  # n번째 이닝 실적
        out = 0

        while out < 3:
            T = scores[numbers[p]]
            if T == 0:
                out += 1
            else:
                board.append(T)

            p += 1  # 다음 타자
            if p == 10:
                p = 1

        if len(board) > 3:
            output += len(board) - 3
            board = board[-3:]

        remain = 0  # 잔반 처리
        for i in range(len(board))[::-1]:
            remain += board[i]
            if remain >= 4:
                output += 1

    mx = max(mx, output)

    return


N = int(input())
players = [[0] + list(map(int, input().split())) for _ in range(N)]
mx = 0
numbers = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
choose_player(1)

print(mx)