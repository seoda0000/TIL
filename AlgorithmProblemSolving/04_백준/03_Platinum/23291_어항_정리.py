"""
3:12 시작
3:24 구상 완료

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
2:40 tc7 디버깅 -> 슬라이싱 오류 수정


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
