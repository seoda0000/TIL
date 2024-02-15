N = int(input())
stairs = [0]*2 + [int(input()) for _ in range(N)]
table = [[0] * (N + 2) for _ in range(2)]  # 한 칸, 두 칸


for i in range(2, N + 2):
    table[0][i] = table[1][i-1] + stairs[i]
    table[1][i] = max(table[0][i-2], table[1][i-2]) + stairs[i]

print(max(table[0][-1], table[1][-1]))  # 마지막 계단을 밟는다
