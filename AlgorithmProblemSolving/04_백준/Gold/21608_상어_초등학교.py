"""
최소값 실수....
3:26 제출 완료
"""

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
N = int(input())
dic = dict()
nums = []
for _ in range(N ** 2):
    num, l1, l2, l3, l4 = map(int, input().split())
    dic[num] = {l1, l2, l3, l4}
    nums.append(num)

arr = [[0] * N for _ in range(N)]

for num in nums:
    mx_like_cnt = blank_cnt = -1
    ti = tj = -1

    for ci in range(N):
        for cj in range(N):

            if arr[ci][cj]: continue

            like = blank = 0

            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]

                if not (0 <= ni < N and 0 <= nj < N): continue

                if arr[ni][nj] == 0:
                    blank += 1
                elif arr[ni][nj] in dic[num]:
                    like += 1

            if mx_like_cnt < like:
                mx_like_cnt = like
                blank_cnt = blank
                ti, tj = ci, cj
            elif mx_like_cnt == like:
                if blank > blank_cnt:
                    blank_cnt = blank
                    ti, tj = ci, cj
    arr[ti][tj] = num

ans = 0
for ci in range(N):
    for cj in range(N):

        num = arr[ci][cj]
        like = 0

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]

            if not (0 <= ni < N and 0 <= nj < N): continue

            if arr[ni][nj] in dic[num]:
                like += 1

        if like > 0:
            ans += 10 ** (like - 1)

print(ans)
