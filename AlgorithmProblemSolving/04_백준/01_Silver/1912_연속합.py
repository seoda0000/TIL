N = int(input())
table = list(map(int, input().split()))

for i in range(1, N):
    if table[i-1] > 0:
        table[i] += table[i-1]
print(max(table))