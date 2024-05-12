"""
실행시간: 188->276
풀이시간: 26분 -> 11분

이전엔 조건 분기로 값을 갱신했는데, 이번엔 그냥 리스트에 넣고 정렬하여 우선순위를 판별했다.
두 방법 모두 알아두면 좋을 것 같다. (모든 값을 정렬하는 것이 더 오래 걸린다.)
"""

"""
11:33 시작
11:36 구상 완료
11:44 구현 완료
"""


def OOB(i, j):
    return not (0 <= i < N and 0 <= j < N)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N = int(input())
arr = [[0] * N for _ in range(N)]
favor_dic = dict()
for _ in range(N * N):
    ipt = list(map(int, input().split()))
    id, favor_lst = ipt[0], ipt[1:]
    favor_dic[id] = favor_lst

    # 칸 찾기
    blank_lst = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]: continue  # 이미 찬 경우
            blank, favor = 0, 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if OOB(ni, nj): continue
                if arr[ni][nj] == 0:
                    blank += 1
                elif arr[ni][nj] in favor_lst:
                    favor += 1
            blank_lst.append((-favor, -blank, i, j))

    blank_lst.sort()

    ei, ej = blank_lst[0][2], blank_lst[0][3]  # 결정
    arr[ei][ej] = id

ans = 0
for i in range(N):
    for j in range(N):
        id = arr[i][j]
        favor_lst = favor_dic[id]
        favor = 0

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if OOB(ni, nj): continue
            if arr[ni][nj] in favor_lst:
                favor += 1

        if favor: ans += 10 ** (favor - 1)
print(ans)

"""
3:26 제출 완료

최소값 실수....
항상 초기화 할 때는 가능하지 않은 값을 넣자
가능한 값을 넣으면 엣지 케이스에 걸릴 가능성이 커진다!!ㅠㅠ
다음부터는 아예 설계 단계에서 초기값을 생각해봐야겠다.
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
