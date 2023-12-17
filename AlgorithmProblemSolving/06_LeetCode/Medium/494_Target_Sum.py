"""
https://leetcode.com/problems/target-sum/submissions/
"""


from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)

			  # n번째 defaultdict: n번째 숫자까지 활용해 만들 수 있는
			  # (숫자: 그 숫자를 만들 수 있는 경우의 수)의 집합

        arr = [defaultdict(int) for _ in range(N)]
        arr[0][nums[0]] += 1
        arr[0][-nums[0]] += 1
        for n in range(1, N):
            for num, cnt in arr[n - 1].items():
                arr[n][num + nums[n]] += cnt
                arr[n][num - nums[n]] += cnt

        return arr[N - 1][target]