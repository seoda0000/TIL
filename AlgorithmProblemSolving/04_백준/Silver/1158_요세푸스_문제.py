N, M = map(int, input().split())
lst = list(range(1, N+1))

i = M-1
ans = []

while lst:
    n = len(lst)
    while i > n-1:
        i -= n
    ans.append(lst[i])
    lst.pop(i)
    i = i-1+M
ans = ", ".join(map(str, ans))
print(f"<{ans}>")