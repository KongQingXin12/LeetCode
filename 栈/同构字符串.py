class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        def disposeStr(target: str) -> str:
            res = ""
            record = {}
            cnt = 0
            for i in target:
                if i not in record:
                    record[i] = cnt
                    cnt += 1
                res += str(record[i])
            return res

        return disposeStr(s) == disposeStr(t)
