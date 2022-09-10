'''
선발 명단
https://www.acmicpc.net/problem/3980
백준 골드5 3980

챔피언스 리그 결승전을 앞두고 있는 맨체스터 유나이티드의 명장 퍼거슨 감독은 이번 경기에 4-4-2 다이아몬드 전술을 사용하려고 한다.

오늘 결승전에 뛸 선발 선수 11명은 미리 골라두었지만, 어떤 선수를 어느 포지션에 배치해야 할지 아직 결정하지 못했다.

수석코치 마이크 펠란은 11명의 선수가 각각의 포지션에서의 능력을 0부터 100까지의 정수로 수치화 했다. 0은 그 선수가 그 포지션에 적합하지 않다는 뜻이다.

이때, 모든 선수의 포지션을 정하는 프로그램을 작성하시오. 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치될 수 없다.
'''
import sys
def input():
    return sys.stdin.readline().rstrip()

def dfs(num, dps):
    global ans
    if num == 11:  # 종료조건
        if dps > ans:
            ans = dps
        return
    for i in range(11):
        if arr[i][num] != 0 and not visited[i]:  # 적합한 선수가 아직 포지션이 없는 경우 선택
            visited[i] = True                    # 기록
            dfs(num+1, dps+arr[i][num])          # 다음 포지션으로
            visited[i] = False                   # clear
    else:
        return

C = int(input())
for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    ans = 0
    dfs(0, 0)
    print(ans)