"""
54퍼에서 틀렸습니다
"""

N = int(input())
lst = list(map(int, input().split()))
ans = 0
mx = 24 * 60
while ans < mx and len(lst) > 1:
    mx1 = lst.pop(lst.index(max(lst)))
    mx2 = lst.pop(lst.index(max(lst)))
    ans += mx2
    if mx1 != mx2:
        lst.append(mx1 - mx2)
if lst:
    ans += lst[0]

if ans > mx:
    ans = -1
print(ans)
