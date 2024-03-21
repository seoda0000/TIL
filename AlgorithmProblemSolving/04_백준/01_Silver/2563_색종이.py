N = int(input())
paper = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(N):
    sj, si = map(int, input().split())

    for i in range(si, si + 10):
        for j in range(sj, sj + 10):
            if paper[i][j] == 0:  # 아직 빈칸일 때
                paper[i][j] = 1  # 색종이 붙이기
                ans += 1  # 넓이 계산
print(ans)
