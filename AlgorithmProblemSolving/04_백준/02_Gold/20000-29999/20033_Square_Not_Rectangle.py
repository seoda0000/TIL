"""
https://www.acmicpc.net/problem/20033

백준 골드4 20033 Square, Not Rectangle

"""

N = int(input())
columns = list(map(int, input().split())) + [0]
stk = []
ans = 0

for h in columns:
    if not stk:  # 처음 넣는 경우
        stk.append([h, 1])

    elif stk[-1][0] > h:  # 작아지는 경우
        mxmnh = 10 ** 9 + 1
        mxmncnt = 0
        while stk and stk[-1][0] >= h:
            ph, cnt = stk.pop()
            mxmnh = min(mxmnh, ph)
            mxmncnt += cnt
            ans = max(ans, min(mxmnh, mxmncnt))
        while stk and stk[-1][0] < ans:
            stk.pop()
        stk.append([h, mxmncnt + 1])

    elif stk[-1][0] == h:  # 같은 높이인 경우
        stk[-1][1] += 1

    else:  # 커지는 경우
        stk.append([h, 1])

print(ans)
