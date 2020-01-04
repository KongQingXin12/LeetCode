from typing import List
import copy


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, n + 1):
                    if dp[i] and (s[i:j] in wordDict):
                        dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    S = Solution()
    print(S.wordBreak(s, wordDict))
