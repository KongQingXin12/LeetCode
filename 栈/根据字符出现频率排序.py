from collections import Counter
from typing import List


class Solution:

    def twoSum(self, nums, target, l, r):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums[l: r + 1])

        start = nums[l - 1]
        dict1 = dict()
        ret = set()
        for i in range(l, r):
            other = target - nums[i]
            if other in dict1:
                ret.add((start, other, nums[i]))
            dict1[nums[i]] = i

        return ret

    def threeSum(self, nums, target, l, r):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums[l: r + 1])
        ret = set()
        start = nums[l - 1]
        dict2 = {}
        for i in range(l, r):
            lll = self.twoSum(nums, target - nums[i], i + 1, r)
            if (lll == set()):
                continue
            for i in lll:
                b = list(i)
                b.append(start)
                b.sort()
                i = tuple(b)
                ret.add(i)
        return ret

    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        ret = set()
        for i in range(n):
            ll = self.threeSum(nums, target - nums[i], i + 1, n)
            if ll == set():
                continue
            ret = ret | ll
        return ret


if __name__ == '__main__':
    s = "Aabb"
    S = Solution()
    print(S.fourSum([-3, -2, -1, 0, 0, 1, 2, 3]
                    , 0))
