# def quick_sort(s, e):
#
#     if s == e or s > N - 1 or e < 0:
#         return
#     target = nums[s]
#     l = s + 1
#     r = e
#     while l <= r:
#         while l < e and l < r:
#             if nums[l] > target:
#                 break
#             else:
#                 l += 1
#         while s < r and l < r:
#             if nums[r] < target:
#                 break
#             else:
#                 r -= 1
#         if l == r:
#             if nums[l] > target:
#                 nums[l - 1], nums[s] = nums[s], nums[l - 1]
#                 quick_sort(s, l - 2)
#                 quick_sort(l, e)
#             else:
#                 nums[l], nums[s] = nums[s], nums[l]
#                 quick_sort(s, l - 1)
#                 quick_sort(l + 1, e)
#             break
#         nums[l], nums[r] = nums[r], nums[l]
#
#     return

def merge_sort(lst):
    N = len(lst)
    if N == 1:
        return lst
    lst1 = merge_sort(lst[:N // 2])
    lst2 = merge_sort(lst[N // 2:])

    p1 = p2 = 0
    N1, N2 = len(lst1), len(lst2)
    sort_lst = []
    while not (p1 == N1 and p2 == N2):

        if p1 == N1:
            for i in range(p2, N2):
                sort_lst.append(lst2[i])
            break
        elif p2 == N2:
            for i in range(p1, N1):
                sort_lst.append(lst1[i])
            break
        else:
            if lst1[p1] <= lst2[p2]:
                sort_lst.append(lst1[p1])
                p1 += 1
            else:
                sort_lst.append(lst2[p2])
                p2 += 1

    return sort_lst


N = int(input())
nums = [int(input()) for _ in range(N)]
# quick_sort(0, N - 1)
nums = merge_sort(nums)
print(*nums, sep='\n')
