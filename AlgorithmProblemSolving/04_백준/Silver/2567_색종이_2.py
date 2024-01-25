"""
https://www.acmicpc.net/problem/2567
백준 실버4 2567 색종이-2

색종이 한칸씩 붙이는 아이디어
"""
N = int(input())
paper = [[0] * 100 for _ in range(100)]
ans = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(N):
    sj, si = map(int, input().split())
    for i in range(si, si + 10):  # 색종이 한칸씩 작업
        for j in range(sj, sj + 10):
            paper[i][j] = 1
            if paper[i][j] == 1:  # 이미 붙인 곳일 경우 skip
                continue
            else:
                minus = 0  # 인근 색종이 수
                for k in range(4):  # 해당 칸의 인근 4방향 탐색
                    ni, nj = i + di[k], j + dj[k]
                    if (0 <= ni < 100) and (0 <= nj < 100) and (paper[ni][nj] == 1):
                        minus += 1
                paper[i][j] = 1  # 색종이 붙이기
                ans -= minus  # 인근에 색종이를 붙이면 해당 면은 기존 테두리에서 제외된다
                ans += 4 - minus  # 인근에 색종이를 붙이면 해당 면은 추가되지도 않는다
print(ans)

"""
빈칸과 인접한 면이 테두리라는 아이디어
"""

N = int(input())
paper = [[0] * 102 for _ in range(102)]
ans = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

for _ in range(N):
    sj, si = map(int, input().split())
    for i in range(si + 1, si + 11):
        for j in range(sj + 1, sj + 11):
            paper[i][j] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if paper[ni][nj] == 0:
                    ans += 1
print(ans)
