def segment(arr, node, left, right):
    if left == right:
        segment_tree[node] = arr[left]
        return segment_tree[node]
    mid = left + (right - left) // 2
    left_val = segment(arr, node * 2, left, mid)
    right_val = segment(arr, node * 2 + 1, mid + 1, right)
    segment_tree[node] = merge(left_val, right_val)
    return segment_tree[node]


def merge(a, b):
    return a + b


def query(start, end, node, left, right):
    if end < left or right < start:  # 쿼리 범위 밖
        return 0

    if start <= left and right <= end:  # 전체가 쿼리 범위 안에 쏙 들어감
        return segment_tree[node]

    mid = left + (right - left) // 2
    left_res = query(start, end, node * 2, left, mid)
    right_res = query(start, end, node * 2 + 1, mid + 1, right)
    return merge(left_res, right_res)


def update(idx, val, node, left, right):  # idx의 숫자에 val만큼 더하기
    if left > idx or right < idx:  # idx와 관련 없는 노드
        return segment_tree[node]
    segment_tree[node] += val
    if left != right:
        mid = left + (right - left) // 2
        update(idx, val, node * 2, left, mid)
        update(idx, val, node * 2 + 1, mid + 1, right)
    return


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
segment_tree = [0] * (len(nums) * 4 + 1)
segment(nums, 1, 0, len(nums) - 1)
print('lst:', nums)
print('segment tree: ', segment_tree)
print('sum 0 to 5: ', query(0, 5, 1, 0, len(nums) - 1))
update(4, 45, 1, 0, len(nums) - 1)
print('segment tree: ', segment_tree)
print('sum 0 to 5: ', query(0, 5, 1, 0, len(nums) - 1))
