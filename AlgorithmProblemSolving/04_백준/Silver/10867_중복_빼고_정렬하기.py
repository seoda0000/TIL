_ = int(input())
nums = list(map(int, input().split()))
print(*sorted(list(set(nums))))