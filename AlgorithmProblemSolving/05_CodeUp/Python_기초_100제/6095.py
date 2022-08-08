# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기

"""
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
"""

N = int(input())

# 바둑돌 위치 리스트 만들기
sit = []
for _ in range(N):
    s1, s2 = map(int, input().split())
    sit.append((s1-1, s2-1))

# 바둑판 만들기
ans = []
for _ in range(19):
    lst = []
    for _ in range(19):
        lst.append(0)
    ans.append(lst)

# 바둑돌 놓기
for i in sit:
    ans[i[0]][i[1]] = 1

#바둑판 출력하기
for i in ans:
    for j in i:
        print(j, end = " ")
    print()