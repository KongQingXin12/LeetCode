from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = 0
        temp = [i for i in nums]
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < len(nums):
            if nums[left] == temp[left]:
                left += 1
            else:
                break
        while right > left:
            if nums[right] == temp[right]:
                right -= 1
            else:
                break
        res = right - left + 1
        return res


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    S = Solution()
    print(S.findUnsortedSubarray(nums))
