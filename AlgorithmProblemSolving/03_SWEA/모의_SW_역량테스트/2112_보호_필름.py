import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def insert(arr, nth, cnt):
    global ans

    if check(arr):
        ans = min(ans, cnt)
    if nth == D:
        return
    if ans <= cnt:
        return

    insert(arr, nth + 1, cnt)

    new_arr = [row[:] for row in arr]
    new_arr[nth] = [0] * W
    insert(new_arr, nth + 1, cnt + 1)

    new_arr[nth] = [1] * W
    insert(new_arr, nth + 1, cnt + 1)

    return -1


def check(arr):  # 합격 여부 return

    for j in range(W):
        num_lst = []
        cnt_lst = []
        for i in range(D):
            if num_lst and num_lst[-1] == arr[i][j]:  # 같은 약품
                cnt_lst[-1] += 1
            else:  # 다른 약품
                num_lst.append(arr[i][j])
                cnt_lst.append(1)

        for cnt in cnt_lst:
            if cnt >= K:
                break
        else:
            return False

    return True


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    ans = D
    insert(arr, 0, 0)
    print(f'#{test_case} {ans}')
