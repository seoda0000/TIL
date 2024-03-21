"""
https://www.acmicpc.net/problem/2630

백준 실버2 2630 색종이 만들기


"""
def findPaper(si, sj, n):
    global ansBlue, ansWhite
    cnt = 0
    for i in range(si, si + n):
        cnt += sum(arr[i][sj:sj + n])
    if cnt == n ** 2:
        ansBlue += 1
    elif cnt == 0:
        ansWhite += 1
    else:
        findPaper(si, sj, n // 2)
        findPaper(si + n // 2, sj, n // 2)
        findPaper(si, sj + n // 2, n // 2)
        findPaper(si + n // 2, sj + n // 2, n // 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ansBlue = ansWhite = 0
findPaper(0, 0, N)

print(ansWhite)
print(ansBlue)
