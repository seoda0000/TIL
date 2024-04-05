"""
실행시간: 136 -> 136
풀이시간: 77분 -> 35분

일전에 문제를 풀면서 zip함수의 특성을 배워서 그렇게 어렵지 않았다.
상돈 프로님이 알려주신 2차원 배열을 1차원으로 만드는 방법 sum(arr, [])이 너무 편하다!
함수화에 집착하지 않고 그대로 구현하니 쉬웠다. 2번만 접으면 되니까 굳이 함수화할 필요는 없다.
"""

"""
9:29 시작
9:38 구상 완료
10:04 구현 완료
"""


def push(arr):
    new_arr = [[0] * len(arr[-1]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cur = arr[i][j]
            for d in range(2):
                ni, nj = i + di[d], j + dj[d]
                if not (0 <= ni < len(arr) and 0 <= nj < len(arr[ni])): continue
                nxt = arr[ni][nj]
                x = abs(nxt - cur) // 5
                if not x: continue
                if cur > nxt:
                    new_arr[i][j] -= x
                    new_arr[ni][nj] += x
                else:
                    new_arr[i][j] += x
                    new_arr[ni][nj] -= x

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += new_arr[i][j]

    c_arr = list(map(list, zip(*arr[::-1])))
    tail = arr[-1][len(arr[0]):]
    flat_lst = sum(c_arr, [])
    return flat_lst + tail


di = [0, 1]
dj = [1, 0]
N, K = map(int, input().split())
flat_lst = list(map(int, input().split()))

t = 0
while True:

    # 밀가루 추가
    mn = min(flat_lst)

    for n in range(N):
        if flat_lst[n] == mn:
            flat_lst[n] += 1

    # 도우 말기

    if N == 1:
        arr = [flat_lst]
    else:
        arr = [[flat_lst[0]]] + [flat_lst[1:]]

        while True:
            w = len(arr[0])
            dough = [a[:w] for a in arr]
            c_dough = list(map(list, zip(*dough[::-1])))
            floor = arr[-1][w:]
            if len(c_dough[0]) > len(floor):
                break
            arr = c_dough + [floor]

    # 꾹 누르기
    flat_lst = push(arr)

    # 두번 접기
    arr = [flat_lst[:N // 2][::-1]] + [flat_lst[N // 2:]]  # 힌번 접기
    up = [a[:N // 2 // 2] for a in arr]
    down = [a[N // 2 // 2:] for a in arr]
    up = list(map(list, zip(*up[::-1])))
    up = list(map(list, zip(*up[::-1])))
    arr = up + down

    # 꾹 누르기
    flat_lst = push(arr)

    t += 1
    if max(flat_lst) - min(flat_lst) <= K:
        break
print(t)

"""
0:00 문제 읽기 시작
0:04 버리고 다른 문제로
1:23 돌아옴
1:34 구상 완료
1:58 어항 돌돌 마는 로직 구현 이후 단위 테스트 -> 오류 발견
2:11 오류 해결 (zip 함수 작동원리 숙지) 후 평평 로직 구현 시작
2:20 평평 로직 구현 이후 단위 테스트 -> 오류 발견
2:24 물고기 나눠주는 로직 수정
2:26 평평 로직 수정  (zip 함수 작동원리 숙지)
2:30 tc 점검 -> 오류 발견 후 문제 정독
2:35 휴식 시작
2:38 휴식 끝
2:40 tc7 디버깅 -> 슬라이싱 오류 수정 및 제출

zip 함수의 원리를 제대로 알지 못하고 썼다. zip함수는 짝이 맞춰진 경우에만 묶어준다. (이외는 무시)
함수의 작동 원리를 파악하고 응용해야 한다.

최대한 함수화를 하느라 오래 걸렸는데 어느 경우에도 적용될 수 있도록 짰으므로 후회는 없다...
다만 하드코딩이 훨씬 빠르고, 다른 경우의 수가 없을 때에는 고려해보도록 해야 겠다.

"""


def roll(bowls):
    rolled_bowls = [[bowls[0]]] + [bowls[1:]]  # 처음 한층 올려주기

    while True:
        up_bowls = list(map(list, zip(*rolled_bowls[::-1])))  # 쌓이는 층
        down_bowls = [rolled_bowls[-1][len(up_bowls):]]  # 바닥 층

        if not down_bowls:  # 아래층 없으면 끝
            break

        if len(up_bowls[0]) > len(down_bowls[0]):  # 위층이 더 넓은 경우 말기 불가
            return rolled_bowls
        else:
            rolled_bowls = up_bowls + down_bowls

    return rolled_bowls


def share_fish(arr_bowls):
    Nb = len(arr_bowls)
    new_arr_bowls = [row[:] for row in arr_bowls]
    for i in range(Nb):
        Mb = len(arr_bowls[i])
        for j in range(Mb):

            # 대상 어항
            cur = arr_bowls[i][j]
            # 인접 어항 찾기
            for d in range(2):
                ni, nj = i + di[d], j + dj[d]

                if nj >= Mb or ni >= Nb: continue

                # 인접 어항
                nxt = arr_bowls[ni][nj]
                dif = abs(cur - nxt) // 5
                if dif == 0: continue

                if cur > nxt:
                    new_arr_bowls[i][j] -= dif
                    new_arr_bowls[ni][nj] += dif
                else:
                    new_arr_bowls[i][j] += dif
                    new_arr_bowls[ni][nj] -= dif

    return new_arr_bowls


def flatten(arr_bowls):
    high_bowls = list(map(list, zip(*arr_bowls[::-1])))
    short_bowls = arr_bowls[-1][len(high_bowls):]
    flatten_bowls = []
    for bowls in high_bowls:
        flatten_bowls += bowls
    return flatten_bowls + short_bowls


def stack(bowls):
    bowls = [bowls]
    for _ in range(2):
        bowls_turned_90 = list(map(list, zip(*bowls[::-1])))

        up_bowls = bowls_turned_90[:len(bowls_turned_90) // 2]
        up_bowls = list(map(list, zip(*up_bowls[::-1])))
        down_bowls = bowls_turned_90[len(bowls_turned_90) // 2:]
        down_bowls = list(map(list, zip(*down_bowls)))[::-1]

        bowls = up_bowls + down_bowls

    return bowls


di = [0, 1]
dj = [1, 0]
N, K = map(int, input().split())
bowls = list(map(int, input().split()))

ans = 0
while True:
    if max(bowls) - min(bowls) <= K:  # 물고기 수 K 이하가 되면 종료
        break
    ans += 1

    # 물고기 수가 가장 적은 어항에 물고기 한 마리 넣기
    mn = min(bowls)
    for i in range(N):
        if bowls[i] == mn:
            bowls[i] += 1

    # 어항 돌돌 말기
    rolled_bowls = roll(bowls)

    # 물고기 수 조절하기
    rolled_bowls = share_fish(rolled_bowls)

    # 다시 1열로 만들기
    bowls = flatten(rolled_bowls)

    # 요상한 방법으로 쌓기
    stacked_bowls = stack(bowls)

    # 물고기 수 조절하기
    stacked_bowls = share_fish(stacked_bowls)

    # 다시 1열로 만들기
    bowls = flatten(stacked_bowls)

print(ans)
