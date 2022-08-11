'''
풍선 터뜨리기
https://www.acmicpc.net/problem/2346
백준 2346 실버 3
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다. 단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다. 각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다. 이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다. 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다. 양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다. 이동할 때에는 이미 터진 풍선은 빼고 이동한다.
'''

import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 풍선 갯수


tmp = 0 # 시작 좌표
ans = []
num = list(range(1, N+1)) # 숫자 리스트
lst= list(map(int, input().split())) # 쪽지 리스트
while num:
    ans.append(num.pop(tmp)) # 터진 풍선 기록
    t = lst.pop(tmp) # 쪽지에 적힌 수
    if t>0: t-=1  # 오른쪽으로 이동할 시 터진 풍선을 반영해 1 빼준다.
    tmp += t # 좌표 이동
    while (tmp<0 or tmp>len(lst)-1) and num: # 범위 밖 좌표 처리. len만큼 더하고 빼준다.
        if tmp<0:
            tmp+=len(lst)
        else:
            tmp-=len(lst)
print(*ans)