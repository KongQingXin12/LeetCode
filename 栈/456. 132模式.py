from typing import List

# 维护一个单调递增站超时
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for i, num in enumerate(nums):
            if len(stack) >= 2 and num < stack[-1]:
                for j in range(i, len(nums)):
                    if nums[j] > stack[0] and nums[j] < stack[-1]:
                        return True
            while stack and num < stack[-1]:
                stack.pop()
            stack.append(num)
        return False
'''

import sys


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        stack = []
        second = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second: return True
            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    nums = [1, 0, 5, -4, -3, 2]
    S = Solution()
    print(S.find132pattern(nums))
