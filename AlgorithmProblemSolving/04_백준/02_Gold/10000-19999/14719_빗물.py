H, W = map(int, input().split())
lst = list(map(int, input().split()))
colored = 0
for floor in range(1, H + 1):
    flag = - 1
    for b in range(len(lst)):
        if lst[b] >= floor:
            if flag >= 0:
                colored += b - flag
                flag = b
            else:
                colored += 1
                flag = b
print(colored - sum(lst))
