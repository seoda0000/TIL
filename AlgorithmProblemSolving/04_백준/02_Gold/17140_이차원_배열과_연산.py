"""
2:50~3:04 구상 완료
3:04~3:39 구현 및 디버깅

구상 및 구현은 쉬웠는데, 생각지 못한 케이스 (중간에 0이 있는 경우)를 디버깅 하느라 시간을 소모했다.
테스트케이스로 한단계만 더 가면 되었을텐데 1단계만 했다;; 3단계는 더 체크해보자

처음엔 하드 코딩으로 가로 세로 경우를 모두 구현했는데, 왠지 실수를 할 것 같아서 함수화시켰다.
훨씬 깔끔하게 코드 검토를 할 수 있었다. transpose 짱!
"""


def do_sort(N, M):  # 정렬 후 열/행 최대 길이 return
    mx = 0
    for i in range(N):  # i번째 행 정렬하기

        nums = set(A[i]) - {0}  # 행에 있는 숫자 목록

        lst = []  # (수, cnt) 리스트
        for num in nums:
            lst.append([num, A[i].count(num)])

        lst.sort(key=lambda x: (x[1], x[0]))

        unpack_lst = []  # 튜플 lst를 unpack해서 1차원 숫자 리스트 얻기
        for l in lst:
            unpack_lst.extend(l)

        length_after = min(100, len(unpack_lst))  # 정렬 후 길이 (최대값: 100)
        mx = max(length_after, mx)  # 가장 긴 길이 갱신

        A[i][:length_after] = unpack_lst  # 앞에서부터 수 채워주기
        if length_after < M:  # 기존 길이보다 짧은 경우: 나머지 길이 0 채우기
            for j in range(length_after, M):
                A[i][j] = 0

    return mx  # 최대 길이 return


R, C, K = map(int, input().split())
R, C = R - 1, C - 1
A = [[0] * 100 for _ in range(100)]
for i in range(3):
    ipt = list(map(int, input().split()))
    A[i][:3] = ipt

N = M = 3  # 초기 행/열 길이

ans = 0
for _ in range(101):
    if A[R][C] == K:  # 정답 조건
        break

    if N >= M:  # 행 기준
        # do R
        M = do_sort(N, M)

    else:  # 열 기준
        # do C
        A = list(map(list, zip(*A)))
        N = do_sort(M, N)
        A = list(map(list, zip(*A)))
    ans += 1
else:
    ans = -1
print(ans)
