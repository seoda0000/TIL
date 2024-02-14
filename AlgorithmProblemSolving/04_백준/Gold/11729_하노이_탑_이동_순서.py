def hanoi(from_idx, to_idx, spare_idx, n):
    if n == 0:
        return
    elif n == 1:
        ans.append((from_idx, to_idx))
    else:
        hanoi(from_idx, spare_idx, to_idx, n - 1)
        hanoi(from_idx, to_idx, spare_idx, 1)
        hanoi(spare_idx, to_idx, from_idx, n - 1)
    return


N = int(input())

ans = []
hanoi(1, 3, 2, N)
print(len(ans))
for a in ans:
    print(*a)
