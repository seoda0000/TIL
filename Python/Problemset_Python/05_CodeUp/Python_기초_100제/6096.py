# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기

"""
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
"""

# 바둑판 입력 받기
ans = []
for _ in range(19):
    ans.append(list(map(int, input().split())))
N = int(input())

# 뒤집을 행과 열 저장
sit = []
for _ in range(N):
    s1, s2 = map(int, input().split())
    sit.append((s1-1, s2-1))

# 행 뒤집기
for i in sit:
    for j in range(19):
        if ans[i[0]][j] == 0:
            ans[i[0]][j] = 1
        else:
            ans[i[0]][j] = 0

# 열 뒤집기
for i in sit:
    for j in range(19):
        if ans[j][i[1]] == 0:
            ans[j][i[1]] = 1
        else:
            ans[j][i[1]] = 0

# 바둑판 출력
for i in ans:
    for j in i:
        print(j, end = " ")
    print()
