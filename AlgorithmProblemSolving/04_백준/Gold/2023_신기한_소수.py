"""
https://www.acmicpc.net/problem/2023
백준 골드5 2023 신기한 소수

수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.

7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다!
수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.

수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

"""


def check(cur_num):  # 소수: True
    for i in range(3, int(cur_num ** (1 / 2)) + 1, 2):  # 홀수만 체크
        if cur_num % i == 0:
            return False
    return True


N = int(input())
num_lst = [list() for _ in range(N)]  # 자릿수별 소수 리스트
num_lst[0] = [2, 3, 5, 7]
back_nums = [1, 3, 7, 9]  # 뒷자리 가능 숫자

for n in range(1, N):
    for pre_num in num_lst[n - 1]:
        pre_num *= 10
        for b in back_nums:
            cur_num = pre_num + b
            if check(cur_num):
                num_lst[n].append(cur_num)

print(*num_lst[N - 1], sep='\n')
