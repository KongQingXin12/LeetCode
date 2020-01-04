from typing import List


# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
#         res = [0] * n
#         stacks = [[]] * n
#         Id, start_or_end, time = logs[0].split(':')
#         if start_or_end == 'end':
#             res[int(Id)] += 1
#             Id = ""
#         else:
#             res[int(Id)] = int(time)
#         for log in logs[1:]:
#             temporary_log = log.split(":")
#             if Id == temporary_log[0]:
#                 if start_or_end != temporary_log[1]:
#                     res[int(Id)] += int(temporary_log[2]) - int(time) + 1
#                     Id = ""
#             elif Id == "":
#                 if temporary_log[1] == 'end':
#                     res[int(temporary_log[0])] += 1
#                 else:
#                     Id, start_or_end, time = logs[0].split(':')
#             else:
#                 if temporary_log[1] == 'start':
#                     res[int(Id)] = int(temporary_log[2]) - int(time)
#                 if temporary_log[1] == 'end':
#                     res[int(temporary_log[0])] += 1
#                 else:
#                     Id, start_or_end, time = log.split(':')
#
#         return res

# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
#         res = [0] * n
#         stacks = [[] for _ in range(n)]
#         running_time = 0
#         for log in logs:
#             temp = log.split(":")
#             Id = int(temp[0])
#             start_or_end = temp[1]
#             time = int(temp[2])
#             if start_or_end == "start":
#                 stacks[Id].append(time)
#             else:
#                 if stacks[Id]:
#                     res[Id] += (time - stacks[Id][-1] + 1 - running_time)
#                     running_time += (time - stacks[Id].pop() + 1 - running_time)
#         return res

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n

        stack.append(int(logs[0].split(":")[0]))
        pre_time = int(logs[0].split(":")[-1])

        for log in logs:
            temp = log.split(":")
            if temp[1] == 'start':
                if stack:
                    res[stack[-1]] += int(temp[-1]) - pre_time
                stack.append(int(temp[0]))
                pre_time = int(temp[-1])
            else:
                res[stack[-1]] += int(temp[-1]) - pre_time + 1
                stack.pop()
                pre_time = int(temp[-1]) + 1
        return res


if __name__ == '__main__':
    n = 2
    logs = ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    S = Solution()
    print(S.exclusiveTime(n, logs))
