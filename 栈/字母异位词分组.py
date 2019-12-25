from typing import List


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = {}
#         for letter in strs:
#             s1 = list(letter)
#             s1.sort()
#             keys = "".join(s1)
#             if keys in res:
#                 res[keys].append(letter)
#             else:
#                 res[keys] = [letter, ]
#         ans = []
#         for key in res:
#             ans.append(res[key])
#         return ans

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return []

        ret = []
        memo = dict()
        k = 0
        for one in strs:
            lone = list(one)
            lone.sort()
            tone = "".join(lone)
            if tone not in memo:
                memo[tone] = k
                k += 1
                ret.append([])
            ret[memo[tone]].append(one)
        return ret


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    S = Solution()
    S.groupAnagrams(strs)
