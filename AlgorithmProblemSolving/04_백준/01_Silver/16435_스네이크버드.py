N, L = map(int, input().split())
hLst = list(map(int, input().split()))
hLst.sort()

for h in hLst:
    if h <= L:
        L += 1
    else:
        break
print(L)
