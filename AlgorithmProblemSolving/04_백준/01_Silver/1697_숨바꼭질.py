# https://www.acmicpc.net/problem/1697
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
lst = [100000] * 200000
answer = 100000
stk = [(N, 0)]
while stk:
    now, time = stk.pop(0)
    if 0 <= now <= 199999:
        if now == K:
            answer = time
            break
        if lst[now] > time:
            lst[now] = time
            stk.append((now + 1, time + 1))
            stk.append((now - 1, time + 1))
            stk.append((now * 2, time + 1))
print(answer)
