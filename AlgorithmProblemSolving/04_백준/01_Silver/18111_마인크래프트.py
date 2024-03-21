"""
백준 실버2
마인크래프트
https://www.acmicpc.net/problem/18111

팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다. 마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.

목재를 충분히 모은 lvalue는 집을 짓기로 하였다. 하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.

lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.

좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

"""
import sys

input = sys.stdin.readline

def sol1():
    N, M, B = map(int, input().split())
    ground = []
    for _ in range(N):
        ground.append(list(map(int, input().split())))

    height = 0
    mn = 256
    sm = 0
    for g in ground:
        sm += sum(g)
        mn = min(mn, min(g))
    ans = sm*2
    for i in range(mn, int((sm+B)/(N*M)) + 1):
        deleteItem = 0
        addItem = 0
        time = 0
        for a in range(N):
            for b in range(M):
                x = ground[a][b]
                if x > i:
                    time += (x - i) * 2
                    deleteItem += (x - i)
                else:
                    time += (i - x)
                    addItem += (i - x)
                if time > ans:
                    break

        if addItem <= deleteItem + B:
            if ans > time:
                ans = time
                height = i
            elif ans == time:
                if height < i:
                    height = i


    print(ans, height)
    return


def sol2():
    N, M, B = map(int, input().split())
    ground = [0]*257
    for _ in range(N):
        row = list(map(int, input().split()))
        for r in row:
            ground[r] += 1

    height = 0
    mn = 257
    sm = 0
    for g in range(len(ground)):
        sm += g*ground[g]
        if mn == 257 and ground[g] != 0:
            mn = g
    ans = sm*2
    for i in range(mn, int((sm+B)/(N*M)) + 1):
        deleteItem = 0
        addItem = 0
        time = 0
        for j in range(257):
            if j > i:
                time += (j-i) * 2 * ground[j]
                deleteItem += (j-i) * ground[j]
            else:
                time += (i - j)* ground[j]
                addItem += (i - j)* ground[j]
            if time > ans:
                break

        if addItem <= deleteItem + B:
            if ans > time:
                ans = time
                height = i
            elif ans == time:
                if height < i:
                    height = i


    print(ans, height)
    return



#sol1()
sol2()
