def make_all_nums(nth, s):  # 서로 다른 숫자로 이루어진 모든 세자리 수 구하기
    if nth == 3:
        nums.append(s)
    else:
        for i in range(1, 10):
            if str(i) in s:
                continue
            make_all_nums(nth + 1, s + str(i))

    return


def match(q, s, b):  # 질문 숫자, 스트라이크, 볼
    m = 0
    while m < len(nums):
        num = nums[m]
        scnt = 0

        for i in range(3):
            if num[i] == q[i]:
                scnt += 1

        bcnt = len(set(num) & set(q)) - scnt

        if scnt != s or bcnt != b:
            nums.pop(m)
        else:
            m += 1


N = int(input())
questions = [list(map(int, input().split())) for _ in range(N)]
questions.sort(key=lambda x: (-x[1], -x[2]))
nums = list()
make_all_nums(0, '')

for q, s, b in questions:
    match(str(q), s, b)  # 질문 조건에 해당하지 않는 숫자를 리스트에서 지우기

print(len(nums))
