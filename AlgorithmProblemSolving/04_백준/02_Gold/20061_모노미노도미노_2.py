"""
3:27 문제 읽기 시작
3:33 문제 읽다 디버깅 떠올라서 다른 문제 감
3:40 다른 문제 풀고 돌아옴
3:42 구상 시작
3:47 큰 단위 구상 완료
3:54 큰 단위 구현 완료 후 휴식
3:58 휴식 끝
4:30 세부 기능 구현 완료
4:35 tc 검토 완료
4:40 틀렸습니다 이후 문제 및 코드 검토
5:28 빈칸 생기면 한층씩 떨어뜨리는 로직 오류 발견 (한번만 함)
5:30 제출 완료

중력 적용을 한번만 해서, 두 칸이 사라졌을 때에 한 칸만 아래로 내려서 오류가 생겼다.
공개된 테스트케이스는 다 맞아서 당황했던 것 같다.
이유를 찾을 수 없어서 시간 낭비를 했는데, 이럴 때에는 공개된 테스트 케이스에서 다루지 않는 상황에 집중하여 확인해보아야 시간 낭비를 하지 않을 것이다.
오류 사항도 문제를 천천히 읽다가 떠올랐다. 애꿎은 코드 괴롭히지 말고 실효성 있는 추가 테케를 생각해보자
중간에 2분간 눈 감고 있었던 게 도움이 된 것 같다
"""


def put(t, j, arr):
    if t == 1:  # 블록 하나
        for i in range(6):
            if arr[i][j]:
                arr[i - 1][j] = 1
                break
        else:
            arr[5][j] = 1
    elif t == 2:  # 가로 블록
        for i in range(6):
            if arr[i][j] or arr[i][j + 1]:
                arr[i - 1][j] = 1
                arr[i - 1][j + 1] = 1
                break
        else:
            arr[5][j] = 1
            arr[5][j + 1] = 1
    else:  # 세로 블록
        for i in range(6):
            if arr[i][j]:
                arr[i - 1][j] = 1
                arr[i - 2][j] = 1
                break
        else:
            arr[5][j] = 1
            arr[4][j] = 1
    return


def check_score(arr):
    score = 0
    for i in range(6):
        if sum(arr[i]) == 4:  # 꽉 채워짐
            score += 1
            arr[i] = [0] * 4  # 점수 올리고 비움
    return score


def check_special(arr):
    cnt = 0
    for i in range(2):
        if sum(arr[i]) > 0:  # 특수칸에 무언가 있다
            cnt += 1

    for i in range(5, 5 - cnt, -1):
        arr[i] = [0] * 4  # 아래 칸 비워준다
    return cnt


def gravity(arr):
    for i in range(1, 6)[::-1]:
        if sum(arr[i]) == 0:  # 텅텅 빔
            arr[i] = arr[i - 1][:]  # 윗층 땡겨옴
            arr[i - 1] = [0] * 4
    return


N = int(input())

blue = [[0] * 4 for _ in range(6)]
green = [[0] * 4 for _ in range(6)]

ans = 0
for _ in range(N):
    t, x, y = map(int, input().split())

    # 둔다
    put(t, y, green)
    if t == 1:
        put(t, x, blue)
    elif t == 2:
        put(3, x, blue)
    elif t == 3:
        put(2, x, blue)

    # 점수 얻는다
    score_green = check_score(green)
    ans += score_green
    score_blue = check_score(blue)
    ans += score_blue

    # 얻었으면 공백 땡긴다
    for _ in range(score_green):
        gravity(green)
    for _ in range(score_blue):
        gravity(blue)

    # 특수칸 처리한다
    cnt_green = check_special(green)
    cnt_blue = check_special(blue)

    # 처리했으면 공백 땡긴다
    for _ in range(cnt_green):
        gravity(green)
    for _ in range(cnt_blue):
        gravity(blue)

print(ans)
cnt = 0
for i in range(6):
    for j in range(4):
        if blue[i][j]:
            cnt += 1
        if green[i][j]:
            cnt += 1
print(cnt)
