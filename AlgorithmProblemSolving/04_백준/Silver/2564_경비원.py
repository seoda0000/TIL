'''
경비원
https://www.acmicpc.net/problem/2564
백준 실버1 2564

동근이는 무인 경비 회사 경비원으로 항상 대기하고 있다가 호출이 들어오면 경비차를 몰고 그 곳으로 달려가야 한다. 동근이가 담당하고 있는 곳은 직사각형 모양의 블록으로 블록 중간을 가로질러 차가 통과할만한 길이 없다. 이 블록 경계에 무인 경비를 의뢰한 상점들이 있다.

블록의 크기와 상점의 개수 및 위치 그리고 동근이의 위치가 주어질 때 동근이의 위치와 각 상점 사이의 최단 거리의 합을 구하는 프로그램을 작성하시오.
'''

def where(d, k):       # (행, 열) 좌표 구하는 함수
    if d == 1:
        i, j = 0, k
    elif d == 2:
        i, j = h, k
    elif d == 3:
        i, j = k, 0
    elif d == 4:
        i, j = k, w
    return i, j

w, h = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dd, dk = map(int, input().split())
di, dj = where(dd, dk)  # 동근이 (행, 열) 좌표
ans = 0
for a in arr:
    d, k = a
    i, j = where(d, k)  # 상점 (행, 열) 좌표
    if d == dd:                  # 같은 방향에 있을 때
        ans += abs(k-dk)
    elif (d-1)//2 == (dd-1)//2:  # 마주보는 방향에 있을 때
        if (d-1)//2 == 0:            # 북남
            ans += min(j + dj + h, w - j + w - dj + h)
        else:                        # 동서
            ans += min(i + di + w, h - i + h - di + w)

    else:                        # 마주보지 않는 다른 방향에 있을 때
        ans += abs(di-i) + abs(dj-j)

print(ans)