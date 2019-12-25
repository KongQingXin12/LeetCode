from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        m = len(nums)
        for i in range(m):
            if nums[i] in record:
                if i - record[nums[i]] <= k:
                    return True
            record[nums[i]] = i
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    S = Solution()
    print(S.containsNearbyDuplicate(nums, k))
