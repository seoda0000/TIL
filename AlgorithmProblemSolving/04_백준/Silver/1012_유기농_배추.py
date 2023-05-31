import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

alst = [1, -1, 0, 0]
blst = [0, 0, 1, -1]
def check(i, j):
    isCheck[i][j] = 1

    for x in range(4):
        if 0<=i+alst[x]<N and 0<=j+blst[x]<M and isCheck[i+alst[x]][j+blst[x]]==0 and ground[i+alst[x]][j+blst[x]]:
            check(i+alst[x], j+blst[x])



T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    isCheck = [[0]*M for _ in range(N)]
    ans = 0
    for _ in range(K):
        a, b = map(int, input().split())
        ground[b][a] = 1
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and isCheck[i][j] == 0:
                ans += 1
                check(i, j)
            isCheck[i][j] = 1
    print(ans)

