import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def to_decimal(s: str):
    if s < 'A':
        return int(s)
    else:
        return dic[s]

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    st = input()
    st += st[:N // 4]
    nums = set()
    for si in range(0, N // 4):

        for i in range(si, si + N, N // 4):
            nums.add(st[i:i + N // 4])
    nums = sorted(list(nums), reverse=True)
    target = nums[K - 1]
    ans = 0
    for t in target:
        ans = (ans * 16 + to_decimal(t))
    print(f'#{test_case} {ans}')
