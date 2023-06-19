# min, max 보다 >, < 비교가 근소하게 빠름

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        N = len(height)

        left = 0
        right = N - 1

        for _ in range(N - 1):
            if height[left] < height[right]:
                if answer < (right - left) * height[left]:
                    answer = (right - left) * height[left]
                left += 1
            else:
                if answer < (right - left) * height[right]:
                    answer = (right - left) * height[right]
                right -= 1

        return answer