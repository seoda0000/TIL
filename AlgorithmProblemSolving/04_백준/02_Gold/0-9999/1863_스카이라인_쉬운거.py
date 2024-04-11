'''
스카이라인 쉬운 거
https://www.acmicpc.net/problem/1863
백준 골드5 1863
도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다.
스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까? 건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정한다.

정확히 건물이 몇 개 있는지 알아내는 것은 대부분의 경우에 불가능하고, 건물이 최소한 몇 채 인지 알아내는 것은 가능해 보인다.
이를 알아내는 프로그램을 작성해 보자.

'''

N = int(input())
s = set()                     # 건물 집합 : 최소 건물이므로 중복되면 안된다.
stk = [] # stack
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b == 0:                # 만약 0이면 집합과 스택에서 건물을 모두 꺼낸다.
        ans += len(s)
        s = set()
        stk = []
    elif stk and stk[-1] > b: # 만약 건물이 낮아지면, 높은 건물을 모두 꺼낸다. (이어질 수 없으므로)
        while stk and stk[-1] > b:
            d = stk.pop()
            if d in s:
                s.remove(d)   # 집합에서 제거할 때만 count
                ans += 1
        s.add(b)    # push
        stk.append(b)
    else:           # push
        s.add(b)
        stk.append(b)
ans += len(s)       # 나머지 계산
print(ans)
