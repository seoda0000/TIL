'''
늑대와 양
https://www.acmicpc.net/problem/16956
백준 실버3 16956

크기가 R×C인 목장이 있고, 목장은 1×1 크기의 칸으로 나누어져 있다. 각각의 칸에는 비어있거나, 양 또는 늑대가 있다. 양은 이동하지 않고 위치를 지키고 있고, 늑대는 인접한 칸을 자유롭게 이동할 수 있다. 두 칸이 인접하다는 것은 두 칸이 변을 공유하는 경우이다.

목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게 하려고 한다. 늑대는 울타리가 있는 칸으로는 이동할 수 없다. 울타리를 설치해보자.

'''

def f():
    global ans
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + a, j + b
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'W':
                        ans = 0
                        return


R, C = map(int, input().split())
arr = [list(input().replace('.', 'D')) for _ in range(R)]
ans = 1
f()
print(ans)
for a in arr:
    print(''.join(a))
