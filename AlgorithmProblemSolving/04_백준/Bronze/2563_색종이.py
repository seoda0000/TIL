'''
색종이
https://www.acmicpc.net/problem/2563
백준 브론즈1 2563

가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.

이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.

이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
'''

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

arr = [[0]*100 for _ in range(100)]
ans = 0

for l in lst:
    x, y = l
    for i in range(x, x+10):
        for j in range(y, y+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                ans += 1

print(ans)