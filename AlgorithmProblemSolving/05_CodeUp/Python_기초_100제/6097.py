# 6097 : [기초-리스트] 설탕과자 뽑기

"""
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
"""

h, w = map(int, input().split())
n = int(input())

# 막대 위치 리스트 만들기
sit = []
for _ in range(n):
    sit.append(tuple(map(int, input().split())))

# 격자판 만들기
ans = []
for _ in range(h):
    lst = []
    for _ in range(w):
        lst.append(0)
    ans.append(lst)

# 막대 놓기

for s in sit:
    stick_len = s[0]
    d = s[1]
    x = s[2]
    y = s[3]
    
    # 가로
    if d == 0:
        
        for i in range(stick_len):
            ans[x-1][y-1+i] = 1
                

    
    # 세로
    if d == 1:

        for i in range(stick_len):
            ans[x-1+i][y-1] = 1

# 격자판 출력하기
for i in ans:
    for j in i:
        print(j, end = " ")
    print()
