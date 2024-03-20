import sys

sys.stdin = open("input.txt", "r")


def check(lst, nth, sm, mx):  # 벌통, 벌통 중 확인할 칸 idx, 벌통의 합, 벌통 수익 합
    global money

    if nth == len(lst):  # 최대 수익 갱신
        money = max(money, mx)
        return

    if sm + lst[nth] <= C:  # 이번 벌통 포함하는 경우
        check(lst, nth + 1, sm + lst[nth], mx + lst[nth] ** 2)
    check(lst, nth + 1, sm, mx)  # 포함하지 않는 경우

    return


def find_max_honey(lst):  # 벌통 리스트로 얻을 수 있는 최대 수익 return
    global money
    money = 0
    check(lst, 0, 0, 0)
    return money


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N - M + 1):
            first = arr[i][j:j + M]  # 첫번째 벌통
            ei, ej = i, j + M - 1  # 첫번째 벌통 마지막 칸

            first_money = find_max_honey(first)  # 첫번째 벌통에서 벌 수 있는 최대 수익
            second_money = 0  # 두번째 벌통에서 벌 수 있는 최대 수익

            # 첫번째 벌통 마지막 칸 다음 칸부터 두번째 벌통 고른다
            for nj in range(ej + 1, N - M + 1):
                second = arr[ei][nj:nj + M]  # 두번째 벌통
                second_money = max(second_money, find_max_honey(second))

            for ni in range(ei + 1, N):
                for nj in range(N - M + 1):
                    second = arr[ni][nj:nj + M]  # 두번째 벌통
                    second_money = max(second_money, find_max_honey(second))

            ans = max(ans, first_money + second_money)  # 최대 수익 갱신

    print(f'#{test_case} {ans}')
