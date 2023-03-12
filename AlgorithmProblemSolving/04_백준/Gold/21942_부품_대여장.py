"""
백준 골드2 21942
https://www.acmicpc.net/problem/21942

송훈이는 로봇 동아리 회원이다. 로봇 동아리에서 필요한 부품이 있을 경우 자유롭게 빌려서 쓰고 다시 돌려놓으면 된다.

하지만 부품 정리를 하다가 부품 관리가 너무 힘들어져 새로운 시스템을 도입하려고 한다.

부품을 빌려갈 경우 부품 대여장에 정보를 반드시 작성해야한다. 또한 빌려간 부품을 반납 할 경우에도 부품 대여장에 정보를 작성해야한다.

또한 대여기간을 정하고 대여기간을 넘길 경우 1분당 벌금을 부여하도록 하는 시스템이다.

만약 대여기간이 5분, 1분당 벌금이 5원이라 했을 때 대여한 시각이 2021년 1월 1일 1시 5분이라면 2021년 1월 1일 1시 10분까지 반납해야한다.

2021년 1월 1일 1시 14분에 반납을 했다면 4분 늦었기 때문에 벌금을 20원을 내야한다.

부품 대여장에 쓰는 형식은 아래와 같다.

yyyy-MM-dd hh:mm [부품 이름] [동아리 회원 닉네임]
아래는 예시를 위한 부품 대여장에 작성된 정보이다. 대여기간이 5분, 벌금은 1원이라 가정하자.

2021-01-01 09:12 arduino tony9402
2021-01-01 09:13 monitor chansol
2021-01-01 09:18 arduino tony9402
2021-01-01 09:18 monitor chansol
위의 정보를 정리하면 아래와 같다.

tony9402가 2021년 1월 1일 오전 9시 12분에 arduino를 빌렸다.
chansol이 2021년 1월 1일 오전 9시 13분에 monitor를 빌렸다.
tony9402가 2021년 1월 1일 오전 9시 18분에 arduino를 반납했다.
chansol이 2021년 1월 1일 오전 9시 18분에 monitor를 반납했다.
tony9402는 1분 늦게 반납했기 때문에 벌금 1원을 내야한다.

부품을 대여할 때 지켜야 하는 조건이 있다.

한 사람이 같은 종류의 부품을 두개 이상 대여하고 있는 상태일 수 없다.
한 사람이 같은 시각에 서로 다른 종류의 부품들을 대여하는 것이 가능하다.
같은 사람이더라도, 대여 기간은 부품마다 별도로 적용된다.
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

N, L, F = input().split()
N, F = int(N), int(F)
rentaltime = ((int(L[:3]) * 24) + int(L[4:6])) * 60 + int(L[7:])
mlst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dic = defaultdict(lambda:defaultdict(int))
ans = defaultdict(int)
for _ in range(N):
    date, time, device, user = input().split()
    month, day = int(date[5:7]), int(date[8:]) # 왜...
    hour, minute = int(time[:2]), int(time[3:])
    timestamp = ((sum(mlst[:month]) + day) * 24 + hour) * 60 + minute

    if dic[user][device] == 0:
        dic[user][device] = timestamp
    else:
        if timestamp - dic[user][device] > rentaltime:
            ans[user] += (timestamp - dic[user][device] - rentaltime) * F
        dic[user][device] = 0

if not ans:
    print(-1)
else:
    usernames = list(ans.keys())
    usernames.sort()
    for u in usernames:
        print(u, ans[u])